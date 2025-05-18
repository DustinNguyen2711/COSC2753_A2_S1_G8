from sklearn.metrics import accuracy_score, f1_score, classification_report

def evaluate_classification(y_true, y_pred):
    print("Accuracy:", accuracy_score(y_true, y_pred))
    print("F1 Score (macro):", f1_score(y_true, y_pred, average='macro'))
    print(classification_report(y_true, y_pred))
