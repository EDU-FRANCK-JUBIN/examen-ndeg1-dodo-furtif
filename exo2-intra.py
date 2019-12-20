# -*- coding: utf-8 -*-


import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

error = ctrl.Antecedent(np.arange(-4, 4, 1), 'error')
error_dot = ctrl.Antecedent(np.arange(-10, 10, 1), 'error_dot')
percent_output = ctrl.Consequent(np.arange(-100, 100, 1), 'percent_output')


error['TH'] = fuzz.trimf(temperature.universe, [-4, -2, 0])
error['JR'] = fuzz.trimf(temperature.universe, [-2, 0, 2])
error['TC'] = fuzz.trimf(temperature.universe, [0, 2, 4])


error_dot['GC'] = fuzz.trimf(humidity.universe, [-10, -5, 0])
error_dot['NC'] = fuzz.trimf(humidity.universe, [-5, 0, 5])
error_dot['GH'] = fuzz.trimf(humidity.universe, [0, 5, 10])


percent_output['C'] = fuzz.trimf(power.universe, [-100, -50, 0])
percent_output['DN'] = fuzz.trimf(power.universe, [-50, 0, 50])
percent_output['H'] = fuzz.trimf(power.universe, [0, 50, 100])


rule1 = ctrl.Rule(error['TH'] | error_dot['GC'], percent_output['C'])
rule2 = ctrl.Rule(error['TH'] | error_dot['NC'], percent_output['C'])
rule3 = ctrl.Rule(error['TH'] | error_dot['GH'], percent_output['C'])
rule4 = ctrl.Rule(error['JR'] | error_dot['GC'], percent_output['H'])
rule5 = ctrl.Rule(error['JR'] | error_dot['NC'], percent_output['DN'])
rule6 = ctrl.Rule(error['JR'] | error_dot['GH'], percent_output['C'])
rule7 = ctrl.Rule(error['TC'] | error_dot['GC'], percent_output['H'])
rule8 = ctrl.Rule(error['TC'] | error_dot['NC'], percent_output['H'])
rule9 = ctrl.Rule(error['TC'] | error_dot['GH'], percent_output['H'])


percent_output_ctrl = ctrl.ControlSystem([rule1,rule1, rule3, rule4, rule5, rule6, rule7, rule8, rule9, rule10, rule11, rule12, rule13, rule14, rule15, rule16])
percent_output_calcul = ctrl.ControlSystemSimulation(power_ctrl)

percent_output_calcul.input['error'] = -1.5
percent_output_calcul.input['error_dot'] = -4
percent_output_calcul.input['error'] = 0.5
percent_output_calcul.input['error_dot'] = 1
percent_output_calcul.input['error'] = -1.5
percent_output_calcul.input['error_dot'] = -1
percent_output_calcul.input['error'] = 0.5
percent_output_calcul.input['error_dot'] = 4

percent_output_calcul.compute()

print(percent_output_calcul.output['percent_output'])

