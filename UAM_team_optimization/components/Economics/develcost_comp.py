import numpy as np
from openmdao.api import ExplicitComponent


class DevelCostComp(ExplicitComponent):

    def setup(self):
        self.add_input('EmptyWeight')
        self.add_input('v_inf')
        self.add_output('DevelCost')

        self.declare_partials('DevelCost', 'EmptyWeight')
        self.declare_partials('DevelCost', 'v_inf')

    def compute(self, inputs, outputs):
        
        EmptyWeight = inputs['EmptyWeight']/9.81
        v_inf = inputs['v_inf']*3.6

        outputs['DevelCost'] = 1.1236 * 67.4 * EmptyWeight**.630 * v_inf**1.3

    def compute_partials(self, inputs, partials):
       
        EmptyWeight = inputs['EmptyWeight']/9.81
        v_inf = inputs['v_inf']*3.6

        partials['DevelCost', 'EmptyWeight'] = 1.1236 * 42.462 * EmptyWeight**-.37 * v_inf**1.3
        partials['DevelCost', 'v_inf'] = 1.1236 *  87.62 * EmptyWeight**.630 * v_inf**.3
