# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
This model is a Random Forest classifier trained to predict whether an individual's salary is greater than $50K or less than or equal to $50K using census dataset. The model was trained using processed numerical and categorical features.

## Intended Use
The intended use of this model is to classify census records into one of two salary categories: `>50K` or `<=50K`. This model is for educational purposes as part of the Udacity Machine Learning DevOps project.

## Training Data
The training data comes from the census dataset provided in the project starter repository. The data includes demographic and employment-related features such as age, workclass, education, occupation, race, sex, hours worked per week, and native country. The dataset was split into training and test sets using an 80/20 split.

## Evaluation Data
The evaluation data is the 20% test split held out from the original census dataset. This test set was not used during model training and was used to evaluate model performance.

## Metrics
_Please include the metrics used and your model's performance on those metrics._
The model was evaluated using precision, recall, and F1 score.
The model achieved the following results on the test set:

- Precision: 0.7419
- Recall: 0.6384
- F1 Score: 0.6863

The model was also evaluated on categorical slices of the data, and the results were saved in `slice_output.txt`.

## Ethical Considerations
This dataset includes sensitive demographic attributes such as race, sex, and native country. Because these features may reflect historical or social bias, predictions from this model should not be used for employment, lending, compensation, or other high-impact decisions. The model may perform differently across demographic groups, so slice-based evaluation is important.

## Caveats and Recommendations
This model is for educational use only. The census dataset may contain missing or unknown values represented by question marks, and the model has not been tuned extensively. Additional work should include more detailed bias analysis, hyperparameter tuning, stronger validation, and monitoring before considering production use.