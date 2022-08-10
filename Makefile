


PID  = 2022S1RSRCommissioning 2018S1RSRCommissioning 2018ARSRCommissioning \
       2014ARSRCommissioning  2015ARSRCommissioning  2016ARSRCommissioning

help:
	@echo PID=$(PID)
	@echo WORK_LMT=$(WORK_LMT)
	@echo Targets here:
	@echo "   runs      - make the run1/run2/... files"
	@echo "   summary   - update the project summary index"


# echo $(lmtinfo.py grep 2022 Science 2021-S1-US-3|awk '{print $2}')


runs:
	./mk_runs.py
	@echo "----"
	@echo "Submit your run script in one of the following methods:"
	@echo "    sbatch_lmtoy.sh RUN1"
	@echo "    parallel --jobs 16 < RUN1"
	@echo "    bash RUN1"
	@echo "when this is done, RUN2 can be started"
	@echo "----"


summary:
	@for p in $(PID); do \
	(echo $$p;  cd $(WORK_LMT)/$$p; mk_summary1.sh > README.html); \
	done
