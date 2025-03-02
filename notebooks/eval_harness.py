import csv

def evaluate_model(trace_file, output_file=None):
    """
    Evaluates model accuracy based on a CSV of traces.

    The CSV should have these columns:
    - `team_name`: The entity being classified.
    - `ground_truth`: The expected classification.
    - `model_output`: The model's prediction.

    Args:
        trace_file (str): Path to the CSV file containing traces.
        output_file (str, optional): Path to save scored results.
    """
    total = 0
    correct = 0
    results = []

    with open(trace_file, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        
        for row in reader:
            team_name = row["team_name"]
            ground_truth = row["ground_truth"].strip().lower()
            model_output = row["model_output"].strip().lower()
            is_correct = ground_truth == model_output

            results.append([team_name, ground_truth, model_output, "✅" if is_correct else "❌"])

            total += 1
            if is_correct:
                correct += 1

    accuracy = (correct / total) * 100 if total > 0 else 0
    print(f"Model Accuracy: {accuracy:.2f}% ({correct}/{total} correct)")

    # Optionally save results with correctness flags
    if output_file:
        with open(output_file, "w", newline="", encoding="utf-8") as outfile:
            writer = csv.writer(outfile)
            writer.writerow(["team_name", "ground_truth", "model_output", "correct"])
            writer.writerows(results)

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Evaluate model accuracy based on traces.")
    parser.add_argument("trace_file", help="Path to the CSV file containing traces.")
    parser.add_argument("--output", help="Path to save scored results (optional).")

    args = parser.parse_args()
    evaluate_model(args.trace_file, args.output)