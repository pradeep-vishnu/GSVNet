#!/bin/bash

# Slurm submission script, 
# GPU job 
# CRIHAN v 1.00 - Jan 2017 
# support@criann.fr

#shared ressources
##SBATCH --share


# Job name
#SBATCH -J "gsv_gta"

# Batch output file
#SBATCH --output output/gsv.o%J

# Batch error file
#SBATCH --error output/gsv.e%J


#SBATCH --partition gpu_k80

#SBATCH --time 48:00:00
#SBATCH --gres gpu:4


#SBATCH --cpus-per-task 4

#SBATCH --mem 20000
# -----
#SBATCH --mail-type ALL
# User e-mail address
##SBATCH --mail-user vishnu.pradeep@esigelec.fr
# environments
# -----

module load python3-DL/3.8.5

# ---------------------------------

# srun
srun python -m torch.distributed.launch ~/repos/GSVNet/main.py --segnet swiftnet --dataset gta --valdataset same --optical-flow-network flownet

#srun python -m ~/repos/GSVNet/main.py/main.py --evaluate 1 --batch-size 1 --resume 1 --dataset gta

# output
mv *.o *.e $SLURM_SUBMIT_DIR/output/

sacct --format=AllocCPUs,AveCPU,MaxRSS,MaxVMSize,JobName -j $SLURM_JOB_ID

