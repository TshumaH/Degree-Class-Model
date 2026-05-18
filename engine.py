import math
import statistics
from typing import Dict, List, Tuple, Any, Optional
from models import StudentProfile, Module

class PredictionEngine:
    def __init__(self, profile: StudentProfile):
        self.profile = profile
        self.all_marks = [entry.mark for entry in profile.transcript]
        self.overall_avg = sum(self.all_marks) / len(self.all_marks) if self.all_marks else 0.0

    def analyze_profile(self) -> Dict[str, Any]:
        # A) Theory vs Technical/Math Split
        theory_marks = []
        tech_marks = []
        
        for entry in self.profile.transcript:
            if 'THEORY' in entry.module.type:
                theory_marks.append(entry.mark)
            else:
                tech_marks.append(entry.mark)
                
        theory_avg = sum(theory_marks) / len(theory_marks) if theory_marks else 0.0
        tech_avg = sum(tech_marks) / len(tech_marks) if tech_marks else 0.0
        
        if theory_avg >= tech_avg + 5:
            strength_profile = 'THEORY_STRONG'
        elif tech_avg >= theory_avg + 5:
            strength_profile = 'TECH_STRONG'
        else:
            strength_profile = 'BALANCED'

        # B) Semester Trend Analysis
        semester_avgs = {}
        for entry in self.profile.transcript:
            key = f"{entry.module.part}-{entry.module.semester}"
            if key not in semester_avgs:
                semester_avgs[key] = []
            semester_avgs[key].append(entry.mark)
            
        # Sort chronologically
        parts_order = {'I': 1, 'II': 2, 'III': 3, 'IV': 4}
        sorted_keys = sorted(semester_avgs.keys(), key=lambda k: (parts_order[k.split('-')[0]], int(k.split('-')[1]) if k.split('-')[1] != 'None' else 0))
        
        ordered_avgs = [sum(semester_avgs[k])/len(semester_avgs[k]) for k in sorted_keys]
        
        trajectory = 'STABLE_MID'
        if len(ordered_avgs) >= 2:
            std_dev = statistics.stdev(ordered_avgs) if len(ordered_avgs) > 1 else 0
            if std_dev > 10:
                trajectory = 'VOLATILE'
            elif all(ordered_avgs[i] < ordered_avgs[i+1] for i in range(len(ordered_avgs)-1)) or (len(ordered_avgs) >= 2 and ordered_avgs[-1] > ordered_avgs[-2] and ordered_avgs[-2] > ordered_avgs[-3] if len(ordered_avgs)>2 else ordered_avgs[-1] > ordered_avgs[-2]):
                trajectory = 'IMPROVING'
            elif all(ordered_avgs[i] > ordered_avgs[i+1] for i in range(len(ordered_avgs)-1)) or (len(ordered_avgs) >= 2 and ordered_avgs[-1] < ordered_avgs[-2] and ordered_avgs[-2] < ordered_avgs[-3] if len(ordered_avgs)>2 else ordered_avgs[-1] < ordered_avgs[-2]):
                trajectory = 'DECLINING'
            else:
                overall_non_volatile_avg = sum(ordered_avgs) / len(ordered_avgs)
                if overall_non_volatile_avg > 65:
                    trajectory = 'STABLE_HIGH'
                else:
                    trajectory = 'STABLE_MID'
                    
        # Format semester_avgs for app.py: "Part I | Semester 1"
        sem_avgs_formatted = {}
        for entry in self.profile.transcript:
            part_str = f"Part {entry.module.part}"
            sem_str = f"Semester {entry.module.semester}" if entry.module.semester else "Industrial Attachment"
            key = f"{part_str} | {sem_str}"
            if key not in sem_avgs_formatted:
                sem_avgs_formatted[key] = []
            sem_avgs_formatted[key].append(entry.mark)
            
        sem_avgs = {k: sum(v)/len(v) for k, v in sem_avgs_formatted.items()}
        
        return {
            'theory_avg': theory_avg,
            'avg_theory': theory_avg, # for app.py compatibility
            'tech_avg': tech_avg,
            'avg_math': tech_avg, # for app.py compatibility
            'strength_profile': strength_profile,
            'strength': strength_profile, # for app.py compatibility
            'trajectory': trajectory,
            'overall_avg': self.overall_avg,
            'overall': self.overall_avg, # for app.py compatibility
            'low_modules': [entry.module.code for entry in self.profile.transcript if entry.mark < 50],
            'sem_avgs': sem_avgs # for app.py compatibility
        }

    def _get_remaining_modules(self) -> List[Module]:
        completed_codes = {entry.module.code for entry in self.profile.transcript}
        remaining = []
        for mod in self.profile.programme.modules:
            if mod.code not in completed_codes and not mod.is_elective:
                remaining.append(mod)
        return remaining

    def generate_scenarios(self, analysis: Dict[str, Any], ia_actual: Optional[float] = None) -> Dict[str, List[Tuple[Module, float]]]:
        remaining = self._get_remaining_modules()
        avg = analysis['overall_avg']
        strength = analysis['strength_profile']
        traj = analysis['trajectory']
        
        mini_project_mark = self.profile.get_module_mark('SCS 2206') or self.profile.get_module_mark('ESH 2211')
        
        pessimistic = []
        realistic = []
        optimistic = []
        
        for mod in remaining:
            is_theory = 'THEORY' in mod.type
            
            # PESSIMISTIC
            if mod.type == 'PRACTICAL':
                p_mark = float(ia_actual) if ia_actual is not None else 65.0
            elif mod.type == 'PROJECT':
                p_mark = 55.0
            else:
                p_mark = avg - 8
                if traj == 'DECLINING': p_mark -= 3
                if strength == 'THEORY_STRONG' and not is_theory: p_mark -= 5
                if strength == 'TECH_STRONG' and is_theory: p_mark -= 3
                p_mark = max(50.0, p_mark)
            pessimistic.append((mod, p_mark))
            
            # REALISTIC
            if mod.type == 'PRACTICAL':
                r_mark = float(ia_actual) if ia_actual is not None else 78.0
            elif mod.type == 'PROJECT':
                if mini_project_mark:
                    r_mark = mini_project_mark
                else:
                    if strength == 'THEORY_STRONG': r_mark = avg
                    elif strength == 'TECH_STRONG': r_mark = avg + 5
                    else: r_mark = avg - 5
            else:
                if (strength == 'THEORY_STRONG' and is_theory) or (strength == 'TECH_STRONG' and not is_theory):
                    r_mark = avg + 2
                elif strength != 'BALANCED':
                    r_mark = avg - 3
                else:
                    r_mark = avg
                    
                if traj == 'IMPROVING': r_mark += 3
                elif traj == 'DECLINING': r_mark -= 3
            realistic.append((mod, r_mark))
            
            # OPTIMISTIC
            if mod.type == 'PRACTICAL':
                o_mark = float(ia_actual) if ia_actual is not None else 85.0
            elif mod.type == 'PROJECT':
                if strength == 'TECH_STRONG': o_mark = 78.0
                elif strength == 'THEORY_STRONG': o_mark = 77.0
                else: o_mark = 75.0
            else:
                o_mark = avg + 8
                if traj == 'IMPROVING': o_mark += 4
                o_mark = min(85.0, o_mark)
            optimistic.append((mod, o_mark))
            
        return {
            'Pessimistic': pessimistic,
            'Realistic': realistic,
            'Optimistic': optimistic
        }

    def _get_class_label(self, mark: float) -> str:
        if mark >= 75: return "First Class 🏆"
        elif mark >= 65: return "Upper Second (2.1) 🥈"
        elif mark >= 60: return "Lower Second (2.2) 🥉"
        elif mark >= 50: return "Pass"
        else: return "Fail ❌"

    def _get_class_color(self, mark: float) -> str:
        if mark >= 75: return "#1E8449" # NUST_GREEN
        elif mark >= 65: return "#0057A8" # NUST_BLUE
        elif mark >= 60: return "#2E86AB"
        elif mark >= 50: return "#E67E22"
        else: return "#C0392B" # NUST_RED

    def calculate_classification(self, scenario_marks: List[Tuple[Module, float]]) -> Dict[str, Any]:
        all_marks_dict = {entry.module.code: entry.mark for entry in self.profile.transcript}
        for mod, mark in scenario_marks:
            all_marks_dict[mod.code] = mark
            
        part2_sum = 0.0
        part2_count = 0
        part4_sum = 0.0
        part4_count = 0
        ia_mark = 0.0
        
        for mod in self.profile.programme.modules:
            if mod.code in all_marks_dict and not mod.is_elective:
                mark = all_marks_dict[mod.code]
                if mod.part == 'II':
                    part2_sum += mark
                    part2_count += 1
                elif mod.part == 'III' or mod.type == 'PRACTICAL':
                    ia_mark = mark
                elif mod.part == 'IV':
                    weight = 2 if mod.type == 'PROJECT' else 1
                    part4_sum += (mark * weight)
                    part4_count += weight
                    
        part2_avg = part2_sum / part2_count if part2_count else 0.0
        part4_avg = part4_sum / part4_count if part4_count else 0.0
        
        weighted_agg = (part2_avg * 0.30) + (ia_mark * 0.20) + (part4_avg * 0.50)
        
        return {
            'part2_avg': round(part2_avg, 1),
            'ia_mark': round(ia_mark, 1),
            'ia': round(ia_mark, 1), # for app.py
            'part4_avg': round(part4_avg, 1),
            'weighted_agg': round(weighted_agg, 1),
            'weighted': round(weighted_agg, 1), # for app.py
            'predicted_class': self._get_class_label(weighted_agg),
            'class': self._get_class_label(weighted_agg), # for app.py
            'color': self._get_class_color(weighted_agg) # for app.py
        }

    def calculate_confidence(self, analysis: Dict[str, Any]) -> float:
        confidence = 50.0
        parts_completed = {entry.module.part for entry in self.profile.transcript}
        
        if 'II' in parts_completed and self.profile.transcript_end_part in ('II', 'III', 'IV') and self.profile.transcript_end_semester == 2:
            confidence += 15
        if 'IV' in parts_completed:
            confidence += 20
        if self.profile.transcript_end_part == 'I':
            confidence -= 20
            
        if analysis['trajectory'] in ['STABLE_HIGH', 'STABLE_MID']:
            confidence += 10
        elif analysis['trajectory'] == 'VOLATILE':
            confidence -= 10
        elif analysis['trajectory'] == 'IMPROVING':
            confidence += 8
        elif analysis['trajectory'] == 'DECLINING':
            confidence -= 8
            
        if analysis['low_modules']:
            confidence -= 5
            
        if any(entry.module.type == 'PROJECT' for entry in self.profile.transcript):
            confidence += 15
        if any(entry.module.type == 'PRACTICAL' for entry in self.profile.transcript):
            confidence += 10
            
        return max(30.0, min(92.0, confidence))

    def run_full_analysis(self, ia_actual: Optional[float] = None) -> Dict[str, Any]:
        analysis = self.analyze_profile()
        scenarios = self.generate_scenarios(analysis, ia_actual=ia_actual)
        
        results = {
            'profile': analysis,
            'predictions': {},
            'confidence': round(self.calculate_confidence(analysis))
        }
        
        for name, scenario_marks in scenarios.items():
            results['predictions'][name] = self.calculate_classification(scenario_marks)
            
        return results
