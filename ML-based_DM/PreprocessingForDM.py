# %%
import pandas as pd
import os

load_path_train = os.path.join(".", "sample_data", "itunes-amazon", "merged_train.csv")
load_path_test = os.path.join(".", "sample_data", "itunes-amazon", "merged_test.csv")
load_path_valid = os.path.join(
    ".", "sample_data", "itunes-amazon", "merged_validation.csv"
)

train_df = pd.read_csv(load_path_train)
test_df = pd.read_csv(load_path_test)
valid_df = pd.read_csv(load_path_valid)
# %%
train_df.head()
# %%
train_df = train_df.rename(columns={"_id": "id"})
train_df = train_df.drop("ltable_id", axis=1)
train_df = train_df.drop("rtable_id", axis=1)
# %%
valid_df = valid_df.rename(columns={"_id": "id"})
valid_df = valid_df.drop("ltable_id", axis=1)
valid_df = valid_df.drop("rtable_id", axis=1)
test_df = test_df.rename(columns={"_id": "id"})
test_df = test_df.drop("ltable_id", axis=1)
test_df = test_df.drop("rtable_id", axis=1)

# %%
column_mapping = {
    "ltable_Song_Name": "left_Song_Name",
    "ltable_Artist_Name": "left_Artist_Name",
    "ltable_Album_Name": "left_Album_Name",
    "ltable_Genre": "left_Genre",
    "ltable_Price": "left_Price",
    "ltable_CopyRight": "left_CopyRight",
    "ltable_Time": "left_Time",
    "ltable_Released": "left_Released",
    "rtable_Song_Name": "right_Song_Name",
    "rtable_Artist_Name": "right_Artist_Name",
    "rtable_Album_Name": "right_Album_Name",
    "rtable_Genre": "right_Genre",
    "rtable_Price": "right_Price",
    "rtable_CopyRight": "right_CopyRight",
    "rtable_Time": "right_Time",
    "rtable_Released": "right_Released",
}

train_df = train_df.rename(columns=column_mapping)
test_df = test_df.rename(columns=column_mapping)
valid_df = valid_df.rename(columns=column_mapping)
# %%
save_path_train = os.path.join(".", "sample_data", "itunes-amazon", "train_d.csv")
train_df.to_csv(save_path_train, index=False)
save_path_valid = os.path.join(".", "sample_data", "itunes-amazon", "valid_d.csv")
valid_df.to_csv(save_path_valid, index=False)
save_path_test = os.path.join(".", "sample_data", "itunes-amazon", "test_d.csv")
test_df.to_csv(save_path_test, index=False)

# %%
