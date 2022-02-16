#!/bin/bash

# Slurm submission script, 
# GPU job 
# CRIHAN v 1.00 - Jan 2017 
# support@criann.fr

#shared ressources
##SBATCH --share


# Job name
#SBATCH -J "GSV_sample_cityscapes_eval"

# Batch output file
#SBATCH --output GSV_02.o%J

# Batch error file
#SBATCH --error GSV_02.e%J


#SBATCH --partition gpu_p100

#SBATCH --time 04:00:00
#SBATCH --gres gpu:1


#SBATCH --cpus-per-task 4

#SBATCH --mem 20000
# -----
#SBATCH --mail-type ALL
# User e-mail address
##SBATCH --mail-user marcos.grassi@groupe-esigelec.org
# environments
# -----

module load python3-DL/3.6.9

# ---------------------------------


cp -ar PyTorch-ENet  $LOCAL_WORK_DIR
cd $LOCAL_WORK_DIR
echo Working directory : $PWD

#add wanted options on the next line
srun python3 main.py --evaluate 1 --batch-size 1 --resume 1

# Move output data to target directory
mkdir $SLURM_SUBMIT_DIR/$SLURM_JOB_ID
mv *.pth *.png $SLURM_SUBMIT_DIR/$SLURM_JOB_ID

sacct --format=AllocCPUs,AveCPU,MaxRSS,MaxVMSize,JobName -j $SLURM_JOB_ID
