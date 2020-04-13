import organ
from organ import ORGAN
from organ import mol_metrics
from rdkit.Chem import AllChem as Chem
import os

class genFDAFragSamples(object):

    def __init__(self, filename, numSamples):
        #print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$'+procedurePath)
        organ_params = {
            'PRETRAIN_GEN_EPOCHS': 600, 'PRETRAIN_DIS_EPOCHS': 20, 'MAX_LENGTH': 60, 'LAMBDA': 0.5, "DIS_EPOCHS": 4,
            'SAMPLE_NUM': 6400, 'WGAN': True}

        # hyper-optimized parameters
        disc_params = {"DIS_L2REG": 0.2, "DIS_EMB_DIM": 32, "DIS_FILTER_SIZES": [
    1, 2, 3, 4, 5, 8, 10, 15], "DIS_NUM_FILTERS": [50, 50, 50, 50, 50, 50, 50, 75], "DIS_DROPOUT": 0.75}

        organ_params.update(disc_params)

        model = ORGAN('FDA-H', 'mol_metrics', params=organ_params)
        ## FDA fragment CSV
        FDAfragCSV = os.path.join(os.path.dirname(organ.__file__), 'data/FDA-H.csv')
        #print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$' + FDAfragCSV)
        ord_dict = model.load_training_set(FDAfragCSV)
        # model.load_prev_pretraining('pretrain_ckpt/qm9-5k_pretrain_ckpt')
        model.set_training_program(['diversity'], [100])
        model.load_metrics()
        # model.load_prev_training(ckpt='qm9-5k_20.ckpt')
        ## save checkpoint in right path.
        checkPointPath = os.path.join(os.path.dirname(organ.__file__), 'checkpoints/FDA-H/FDA-H_99.ckpt')
        model.load_prev_training(ckpt=checkPointPath)
        samples = model.generate_samples(numSamples)
        # print('$$$$$$$$$$$$$$$$$$$$', )
        # store in set
        lineSet = set()
        #f = open('tmpSmiles.txt', 'w')
        def mol_from_mb(mb):
            if Chem.MolFromSmiles(mb) is None:
                return
            # print('%%%%%%%%%%%%%%%%%%%%%%%%%%% ', res)
            else:
                # the find collection does not repeat.
                lineSet.add(mb)

        for i in range(len(samples)):
            if samples[i] is not None:
                mol_from_mb(mol_metrics.decode(samples[i], ord_dict))


        # reach the numSamples
        count = 0
        # Get number of set
        num_lines = len(lineSet)
        # repeat generate process
        if (numSamples > 100000):
            tmpGen = int(numSamples / 10)
            totalcount = 1000
        else:
            tmpGen = numSamples
            totalcount = 100

        while True:
            num_lines = len(lineSet)
            if num_lines >= numSamples:
                break

            samples = model.generate_samples(tmpGen)

            for k in range(len(samples)):
                if mol_metrics.decode(samples[k], ord_dict) not in lineSet:
                    mol_from_mb(mol_metrics.decode(samples[k], ord_dict))

            count += 1

            ## break until 100 time repeat.
            if(count > totalcount):
                break

        # write the pointed number in file.
        count = 0
        # Write set into file.
        outFile = open(filename, "w")

        for i in range(len(lineSet)):
            if (count >= numSamples):
                break

            outFile.write(list(lineSet)[i]+ '\n')
            outFile.flush()
            count += 1

        outFile.close()

        del count
        del lineSet


class genFDAMolSamples(object):

    def __init__(self, filename, numSamples):
        #print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$'+procedurePath)
        organ_params = {
    'PRETRAIN_GEN_EPOCHS': 1200, 'PRETRAIN_DIS_EPOCHS': 20, 'MAX_LENGTH': 60, 'LAMBDA': 0.5, "DIS_EPOCHS": 2, 'SAMPLE_NUM': 640, 'WGAN':True}

        # hyper-optimized parameters
        disc_params = {"DIS_L2REG": 0.2, "DIS_EMB_DIM": 32, "DIS_FILTER_SIZES": [
    1, 2, 3, 4, 5, 8, 10, 15], "DIS_NUM_FILTERS": [50, 50, 50, 50, 50, 50, 50, 75], "DIS_DROPOUT": 0.75}

        organ_params.update(disc_params)

        model = ORGAN('FDA1884', 'mol_metrics', params=organ_params)
        ## FDA fragment CSV
        FDAfragCSV = os.path.join(os.path.dirname(organ.__file__), 'data/FDA1884.csv')
        #print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$' + FDAfragCSV)
        ord_dict = model.load_training_set(FDAfragCSV)
        # model.load_prev_pretraining('pretrain_ckpt/qm9-5k_pretrain_ckpt')
        model.set_training_program(['druglikeliness'], [120])
        model.load_metrics()
        # model.load_prev_training(ckpt='qm9-5k_20.ckpt')
        ## save checkpoint in right path.
        checkPointPath = os.path.join(os.path.dirname(organ.__file__), 'checkpoints/FDA1884/FDA1884_119.ckpt')
        model.load_prev_training(ckpt=checkPointPath)
        samples = model.generate_samples(numSamples)
        # print('$$$$$$$$$$$$$$$$$$$$', )
        # store in set
        lineSet = set()
        #f = open('tmpSmiles.txt', 'w')
        def mol_from_mb(mb):
            if Chem.MolFromSmiles(mb) is None:
                return
            # print('%%%%%%%%%%%%%%%%%%%%%%%%%%% ', res)
            else:
                # the find collection does not repeat.
                lineSet.add(mb)

        for i in range(len(samples)):
            if samples[i] is not None:
                mol_from_mb(mol_metrics.decode(samples[i], ord_dict))


        # reach the numSamples
        count = 0
        # Get number of set
        num_lines = len(lineSet)
        # repeat generate process
        if (numSamples > 100000):
            tmpGen = int(numSamples / 10)
            totalcount = 1000
        else:
            tmpGen = numSamples
            totalcount = 100

        while True:
            num_lines = len(lineSet)
            if num_lines >= numSamples:
                break

            samples = model.generate_samples(tmpGen)

            for k in range(len(samples)):
                if mol_metrics.decode(samples[k], ord_dict) not in lineSet:
                    mol_from_mb(mol_metrics.decode(samples[k], ord_dict))

            count += 1

            ## break until 100 time repeat.
            if(count > totalcount):
                break

        # write the pointed number in file.
        count = 0
        # Write set into file.
        outFile = open(filename, "w")

        for i in range(len(lineSet)):
            if (count >= numSamples):
                break

            outFile.write(list(lineSet)[i]+ '\n')
            outFile.flush()
            count += 1

        outFile.close()

        del count
        del lineSet

class genZINCMolSamples(object):

    def __init__(self, filename, numSamples):
        #print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$'+procedurePath)
        organ_params = {
    'PRETRAIN_GEN_EPOCHS': 250, 'PRETRAIN_DIS_EPOCHS': 20, 'MAX_LENGTH': 60, 'LAMBDA': 0.5, "DIS_EPOCHS": 2, 'SAMPLE_NUM': 64000, 'WGAN':True}

        # hyper-optimized parameters
        disc_params = {"DIS_L2REG": 0.2, "DIS_EMB_DIM": 32, "DIS_FILTER_SIZES": [
    1, 2, 3, 4, 5, 8, 10, 15], "DIS_NUM_FILTERS": [50, 50, 50, 50, 50, 50, 50, 75], "DIS_DROPOUT": 0.75}

        organ_params.update(disc_params)

        model = ORGAN('ZINC', 'mol_metrics', params=organ_params)
        ## FDA fragment CSV
        FDAfragCSV = os.path.join(os.path.dirname(organ.__file__), 'data/zinc.csv')
        #print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$' + FDAfragCSV)
        ord_dict = model.load_training_set(FDAfragCSV)
        # model.load_prev_pretraining('pretrain_ckpt/qm9-5k_pretrain_ckpt')
        model.set_training_program(['druglikeliness'], [100])
        model.load_metrics()
        # model.load_prev_training(ckpt='qm9-5k_20.ckpt')
        ## save checkpoint in right path.
        checkPointPath = os.path.join(os.path.dirname(organ.__file__), 'checkpoints/ZINC/ZINC_99.ckpt')
        model.load_prev_training(ckpt=checkPointPath)
        samples = model.generate_samples(numSamples)
        # print('$$$$$$$$$$$$$$$$$$$$', )
        # store in set
        lineSet = set()
        #f = open('tmpSmiles.txt', 'w')
        def mol_from_mb(mb):
            if Chem.MolFromSmiles(mb) is None:
                return
            # print('%%%%%%%%%%%%%%%%%%%%%%%%%%% ', res)
            else:
                # the find collection does not repeat.
                lineSet.add(mb)

        for i in range(len(samples)):
            if samples[i] is not None:
                mol_from_mb(mol_metrics.decode(samples[i], ord_dict))


        # reach the numSamples
        count = 0
        # Get number of set
        num_lines = len(lineSet)
        # repeat generate process
        if (numSamples > 100000):
            tmpGen = int(numSamples / 10)
            totalcount = 1000
        else:
            tmpGen = numSamples
            totalcount = 100

        while True:
            num_lines = len(lineSet)
            if num_lines >= numSamples:
                break

            samples = model.generate_samples(tmpGen)

            for k in range(len(samples)):
                if mol_metrics.decode(samples[k], ord_dict) not in lineSet:
                    mol_from_mb(mol_metrics.decode(samples[k], ord_dict))

            count += 1

            ## break until 100 time repeat.
            if(count > totalcount):
                break

        # write the pointed number in file.
        count = 0
        # Write set into file.
        outFile = open(filename, "w")

        for i in range(len(lineSet)):
            if (count >= numSamples):
                break

            outFile.write(list(lineSet)[i]+ '\n')
            outFile.flush()
            count += 1

        outFile.close()

        del count
        del lineSet