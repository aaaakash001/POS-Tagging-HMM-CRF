from collections import defaultdict
import pandas as pd

df = pd.read_csv('/Users/aakashagarwal/Documents/GitHub/CS626-HMM-POS_aakash/error_analysis/wrong_predictions_fold_1.csv')

Correct_Wrong_Tags = df['Actual_Pred_Wrong_Tag']

correct_tag_wrong_tag = dict()

# Initialize dictionaries to count tags
preceding_counts = defaultdict(lambda: defaultdict(int))
proceeding_counts = defaultdict(lambda: defaultdict(int))
total_counts = defaultdict(int)


for lists in Correct_Wrong_Tags:
    for list in lists.split(', '):
        correct_tag_wrong_tag[list] = correct_tag_wrong_tag.get(list,0)+1

sorted_dict = dict(sorted(correct_tag_wrong_tag.items(), key=lambda item: item[1]))

print(sorted_dict)


import pandas as pd

# Initialize a list to store results
results = []

# Iterate through each row of the DataFrame
for index, row in df.iterrows():
    actual_tags = row['Actual_Tags'].split(', ')
    predicted_tags = row['Predicted_Tags'].split(', ')
    wrong_tags = row['Actual_Pred_Wrong_Tag'].split(', ')
    
    for wrong_tag in wrong_tags:
        actual_wrong_tag, predicted_wrong_tag = wrong_tag.split('_')
        
        # Find all occurrences of wrong tags in the actual and predicted lists
        for i, tag in enumerate(actual_tags):
            if tag == actual_wrong_tag and (i < len(predicted_tags) and predicted_tags[i] == predicted_wrong_tag):
                # Determine preceding and proceeding tags
                preceding_tag = actual_tags[i - 1] if i > 0 else None
                proceeding_tag = actual_tags[i + 1] if i < len(actual_tags) - 1 else None
                
                # Append the result to the list
                results.append({
                    'Index': index,
                    'Position': i,
                    'Wrong_Tag': wrong_tag,
                    'Preceding_Tag': preceding_tag,
                    'Proceeding_Tag': proceeding_tag
                })
                
                # Update counts
                if preceding_tag:
                    preceding_counts[wrong_tag][preceding_tag] += 1
                if proceeding_tag:
                    proceeding_counts[wrong_tag][proceeding_tag] += 1
                    
                total_counts[wrong_tag] += 1

# Convert the results to a DataFrame and save to a new CSV file
results_df = pd.DataFrame(results)
results_df.to_csv('./results.csv', index=False)  # Update this with your desired output file path

print("Processing complete. Results saved to 'results.csv'.")


# Print counts for each tag combination
print("\nPreceding Tag Counts:")
for wrong_tag, counts in preceding_counts.items():
    print(f"\nWrong Tag: {wrong_tag}")
    for tag, count in counts.items():
        print(f"  Preceding Tag: {tag}, Count: {count}")
    # Print total count for verification
    print(f"Total Count for '{wrong_tag}': {total_counts[wrong_tag]}")

print("\nProceeding Tag Counts:")
for wrong_tag, counts in proceeding_counts.items():
    print(f"\nWrong Tag: {wrong_tag}")
    for tag, count in counts.items():
        print(f"  Proceeding Tag: {tag}, Count: {count}")