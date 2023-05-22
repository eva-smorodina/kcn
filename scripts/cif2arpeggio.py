from multiprocessing import Pool
import subprocess
import os
import time

cpus = 10

structure_path = '../structures_cif/'
output_path = '../structures_arpeggio/'

#l1 = os.listdir(structure_path) 
#l2 = os.listdir(output_path) 
#structures = [x for x in l1 if x.split('.')[0] + '.json' not in l2]

structures = os.listdir(structure_path)

#print(len(l1))
#print(len(l2))

print(len(structures))  
    
def run(structure):
    print(structure)
    cmd = ('arpeggio -o {} {}'.format(output_path, structure_path + structure))
    subprocess.call(cmd, shell = True) 
      
if __name__ == '__main__':
    pool = Pool(processes = cpus)
    results = pool.map(run, structures)
    pool.close()
    pool.join()
