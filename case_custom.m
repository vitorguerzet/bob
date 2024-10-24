
function mpc = case_custom
mpc.version = '2';
mpc.baseMVA = 100;

%% bus data
%	bus_i	type	Pd	Qd	Gs	Bs	area	Vm	Va	baseKV	zone	Vmax	Vmin
mpc.bus = [
1	3	0	0	0	0	1	1	0	230	1	1.1	0.94;
2	1	0	0	0	0	1	1.045	0	230	1	1.06	0.94;
3	2	5	0	0	0	1	1.01	0	13.8	1	1.06	0.94
];

%% generator data
%	bus	Pg	Qg	Qmax	Qmin	Vg	mBase	status	Pmax	Pmin	Pc1	Pc2	Qc1min	Qc1max	Qc2min	Qc2max	ramp_agc	ramp_10	ramp_30	ramp_q	apf
mpc.gen = [
1	10	0	30	-30	1.06	100	1	10	0	0	0	0	0	0	0	0	0	0	0	0;
2	10	0	30	-30	1.045	100	1	10	0	0	0	0	0	0	0	0	0	0	0	0
];

%% branch data
%	fbus	tbus	r	x	b	rateA	rateB	rateC	ratio	angle	status	angmin	angmax
mpc.branch = [
1	2	0.017	0.092	0.158	250	250	250	0	0	1	-360	360;
2	3	0.01	0.003	0.0002	100	100	100	16.67	-30	1	-360	360
];

%% generator cost data
% model startup shutdown n c(n-1) ... c0
mpc.gencost = [
2	0	0	3	0.02	2.0	0;
2	0	0	3	0.0175	1.75	0
];
