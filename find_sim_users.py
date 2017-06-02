import os
import numpy as np

DIRECTORY = "/Users/Raunaq/Downloads/facebook"

def select_circle():
	max_nodes = 0
	max_idx = 0
	all_relevant_idxs = []
	row_max = []
	count = 0
	for filename in os.listdir(DIRECTORY):
		if filename.endswith(".featnames"):
			relevant_feats_idxs = []
			with open(DIRECTORY+"/"+filename, "rb") as file:
				for line in file.readlines():
					feat = line.split()
					featname = feat[1].split(";")
					if featname[0] == "birthday":
						feat_idx = feat[3]
						relevant_feats_idxs.append(int(feat_idx))
			# print filename
			# print relevant_feats_idxs
			circle_number = filename.split(".")[0]
			feat_file = DIRECTORY+"/"+circle_number+".feat"
			feats_matrix = None
			try:
				with open(feat_file, "rb") as file_1:
					for line_1 in file_1.readlines():
						curr_feats = line_1.split()[1:]
						curr_feats = map(int, curr_feats)
						curr_feats = np.array(curr_feats)[relevant_feats_idxs]
						# print curr_feats
						if feats_matrix is None:
							feats_matrix = curr_feats
						else:
							feats_matrix = np.vstack((feats_matrix, curr_feats))
				curr_max = np.max(np.sum(feats_matrix, axis = 0))
				max_row = np.argmax(np.sum(feats_matrix, axis = 0))
				row_max.append(max_row)
				if curr_max > max_nodes:
					max_nodes = curr_max
					max_idx = count
			except:
				pass
			all_relevant_idxs.append(relevant_feats_idxs)
			count += 1
	return all_relevant_idxs[max_idx], row_max[max_idx]


def get_relevant_nodes(filename, relevant_feats_idxs, best_row):
	relevant_nodes = []
	feats_matrix = None
	with open(DIRECTORY+"/"+filename, "rb") as file:
		for line in file.readlines():
			curr_feats = line.split()[1:]
			curr_feats = map(int, curr_feats)
			curr_feats = np.array(curr_feats)[relevant_feats_idxs]
			if curr_feats[best_row] == 1:
				relevant_nodes.append(line.split()[0])
	return relevant_nodes


relevant_idxs, best_row = select_circle()
relevant_nodes = get_relevant_nodes("107.feat", relevant_idxs, best_row)
