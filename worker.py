import os 
import gearman 
import math 

class CustomGearmanWorker(gearman.GearmanWorker):
    def on_job_execute(self, current_job):
        print "Job started"       
        return super(CustomGearmanWorker, self).on_job_execute(current_job)
    
def task_callback(gearman_worker, job):      
    print job.data     
    return job.data 

new_worker = CustomGearmanWorker(['127.0.0.1:4730'])#localhost name  
new_worker.register_task("dict", task_callback) #taskname+funtionname 
new_worker.work()
