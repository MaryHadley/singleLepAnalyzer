
input = 'dummy.root'

rFileName = input.split('/')[-1][:-5]
                                                                                                                                          
def get_model():
    model = build_model_from_rootfile(input,include_mc_uncertainties=True)#,histogram_filter = (lambda s: s.count('jec')==0 and s.count('jer')==0)

    model.fill_histogram_zerobins()
    model.set_signal_processes('sig')
    
    procs = model.processes
    obsvs = model.observables.keys()

    for obs in obsvs:
		if 'isE' in obs:
			model.add_lognormal_uncertainty('elTrigSys', math.log(1.03), '*', obs)
			model.add_lognormal_uncertainty('elIdSys', math.log(1.01), '*', obs)
			model.add_lognormal_uncertainty('elIsoSys', math.log(1.01), '*', obs)
		elif 'isM' in obs:
			model.add_lognormal_uncertainty('muTrigSys', math.log(1.011), '*', obs)
			model.add_lognormal_uncertainty('muIdSys', math.log(1.011), '*', obs)
			model.add_lognormal_uncertainty('muIsoSys', math.log(1.03), '*', obs)
    model.add_lognormal_uncertainty('lumiSys', math.log(1.062), '*', '*')

    try: model.add_lognormal_uncertainty('topSys',  math.log(1.20), 'top', '*')
    except: pass
    try: model.add_lognormal_uncertainty('ewkSys',  math.log(1.20), 'ewk', '*')
    except: pass
    try: model.add_lognormal_uncertainty('qcdSys',  math.log(1.20), 'qcd', '*')
    except: pass
    try: model.add_lognormal_uncertainty('ttbarSys',math.log(1.10), 'ttbar', '*')
    except: pass
    try: model.add_lognormal_uncertainty('ttbbSys', math.log(1.10), 'ttbb', '*')
    except: pass
    try: model.add_lognormal_uncertainty('ttllSys', math.log(1.10), 'ttll', '*')
    except: pass
    try: model.add_lognormal_uncertainty('wjetsSys',math.log(1.20), 'wjets', '*')
    except: pass
    try: model.add_lognormal_uncertainty('wbSys',   math.log(1.20), 'wjetsb', '*')
    except: pass
    try: model.add_lognormal_uncertainty('wcSys',   math.log(1.20), 'wjetsc', '*')
    except: pass
    try: model.add_lognormal_uncertainty('wlSys',   math.log(1.20), 'wjetsl', '*')
    except: pass
    try: model.add_lognormal_uncertainty('sigSys',  math.log(1.10), 'sig', '*')
    except: pass
			
    return model

model = get_model()

##################################################################################################################

model_summary(model)

plot_exp, plot_obs = bayesian_limits(model,'all', n_toy = 5000, n_data = 500)
#plot_exp, plot_obs = bayesian_limits(model,'all', n_toy = 100000, n_data = 1000)
#plot_exp, plot_obs = bayesian_limits(model,'expected')
plot_exp.write_txt('limits_'+rFileName+'_expected.txt')
plot_obs.write_txt('limits_'+rFileName+'_observed.txt')

report.write_html('htmlout_'+rFileName)
