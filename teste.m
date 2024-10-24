
function mpc = case_custom
mpc.version = '2';
mpc.baseMVA = 100;

%% bus data
%	bus_i	type	Pd	Qd	Gs	Bs	area	Vm	Va	baseKV	zone	Vmax	Vmin
mpc.bus = [
0.0	3.0	0.0	0.0	0.0	0.0	1.0	13800.0	0.0	13800.0	1.0	1.3	0.96;
1.0	1.0	50.0	10.0	0.0	0.0	1.0	1.03	0.0	13.8	1.0	1.2	0.97
];

%% generator data
%	bus	Pg	Qg	Qmax	Qmin	Vg	mBase	status	Pmax	Pmin	Pc1	Pc2	Qc1min	Qc1max	Qc2min	Qc2max	ramp_agc	ramp_10	ramp_30	ramp_q	apf
mpc.gen = [

];

%% branch data
%	fbus	tbus	r	x	b	rateA	rateB	rateC	ratio	angle	status	angmin	angmax
mpc.branch = [
0.0	1.0	0.022	0.0045	0.0	250.0	300.0	450.0	1.0	0.0	1.0	360.0	360.0
];

%% generator cost data
% model startup shutdown n c(n-1) ... c0
mpc.gencost = [

];
