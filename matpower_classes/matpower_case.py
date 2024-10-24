class MatpowerCase:
    def __init__(self, case_name, version=2, baseMVA=100):
        self.name = case_name
        self.version = version
        self.baseMVA = baseMVA
        self.buses = []
        self.generators = []
        self.branches = []
        self.transformers = []
        self.gencost = []

    def add_bus(self, bus):
        self.buses.append(bus)

    def add_generator(self, generator):
        self.generators.append(generator)

    def add_branch(self, branch):
        self.branches.append(branch)

    def add_transformer(self, transformer):
        self.transformers.append(transformer)
        
    def add_gencost(self, gencost):
        self.gencost.append(gencost)

    def generate_case(self):
        buses_str = ";\n".join([str(bus) for bus in self.buses])
        generators_str = ";\n".join([str(generator) for generator in self.generators])
        branches_str = ";\n".join([str(branch) for branch in self.branches])
        if self.transformers:
            transf_str = ";\n".join([str(transf) for transf in self.transformers])
            branches_str += ";\n" + transf_str
        gencosts_str = ";\n".join([str(cost) for cost in self.gencost])

        case_template = f"""
function mpc = {self.name}
mpc.version = '{self.version}';
mpc.baseMVA = {self.baseMVA};

%% bus data
%	bus_i	type	Pd	Qd	Gs	Bs	area	Vm	Va	baseKV	zone	Vmax	Vmin
mpc.bus = [
{buses_str}
];

%% generator data
%	bus	Pg	Qg	Qmax	Qmin	Vg	mBase	status	Pmax	Pmin	Pc1	Pc2	Qc1min	Qc1max	Qc2min	Qc2max	ramp_agc	ramp_10	ramp_30	ramp_q	apf
mpc.gen = [
{generators_str}
];

%% branch data
%	fbus	tbus	r	x	b	rateA	rateB	rateC	ratio	angle	status	angmin	angmax
mpc.branch = [
{branches_str}
];

%% generator cost data
% model startup shutdown n c(n-1) ... c0
mpc.gencost = [
{gencosts_str}
];
"""
        
        return case_template

    def save_case_file(self, filename):
        case_data = self.generate_case()
        with open(filename, 'w') as file:
            file.write(case_data)
        print(f"Arquivo de caso MATPOWER gerado com sucesso: {filename}")
