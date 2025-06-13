# Decision Tool
# Copyright (c) 2025 Nathaniel Robson, Ph.D
# 
# This code is licensed under the MIT License.
# See the LICENSE file in the GitHub repository root for full terms.
#
# If you use or modify this code, please acknowledge the original author.

MIN_SCORE = 0    # lowest score user should enter
MAX_SCORE = 5    # highest score user should enter

def print_instructions():
    print("""
             This tool facilitates multi-level criteria analysis to make decisions.\n\n
             In general, you specify options i, criteria j and factors (sub-criteria) k.\n
             You then give the criteria overall weights and factors weights within their criteria.\n
             Finally, you score each option according to the criteria-factor pairs.\n
             The program computes the weighted score for each option i using:\n\n
             Total Scoreᵢ = Σⱼ [ CriterionWeightⱼ × Σₖ (Scoreᵢⱼₖ × FactorWeightₖ) ]\n\n
             The optimal option is that which has the highest weighted score.\n\n
             Factor specification is flexible, so criteria can have different numbers of factors,\n
             or even no factors.  If no factors are specified for all criteria the analysis reduces\n
             to the standard option-criteria decision matrix method.\n\n
             The user may select one of three hardcoded examples, or input their own data.\n\n
         """)

# This function gathers hardcoded values for options, criteria, criterion_weights and scores.
# Once they have been assigned, the gathered information is all returned.

def simple_2_by_2_example():
    
    # Hardcoded values for simple 2 by 2 example

    MIN_SCORE = 0 # reset for consistency with hardcoded scores
    MAX_SCORE = 5 # reset for consistency with hardcoded scores

    options = [
        "Project A",
        "Project B",
        "Project C"
    ]

    criteria = [
        "Cost",
        "Quality",
        "Speed"
    ]

    criterion_weights = {
        "Cost": 3,
        "Quality": 5,
        "Speed": 2
    }

    # For direct scoring, each criterion is its own "factor"
    factors = {criterion: [criterion] for criterion in criteria}
    factor_weights = {criterion: {criterion: 1.0} for criterion in criteria}

    # Structure: scores[option][criterion][criterion] = score
    scores = {
        "Project A": {
            "Cost":    {"Cost":    5},
            "Quality": {"Quality": 3},
            "Speed":   {"Speed":   2}
        },
        "Project B": {
            "Cost":    {"Cost":    2},
            "Quality": {"Quality": 5},
            "Speed":   {"Speed":   4}
        },
        "Project C": {
            "Cost":    {"Cost":    3},
            "Quality": {"Quality": 4},
            "Speed":   {"Speed":   5}
        }
    }

    return options, criteria, criterion_weights, factors, factor_weights, scores

# This function gathers hardcoded values for options, criteria, criterion_weights, factors, 
# factor_weights, and scores.  Once they have been assigned, the gathered information is all returned.

def mixed_factors_example():

    # Hardcoded values for mixed factor example
    
    MIN_SCORE = 0
    MAX_SCORE = 5

    options = [
        "System Alpha",
        "System Beta",
        "System Gamma"
    ]

    criteria = [
        "Cost Efficiency",      # 3 factors
        "User Experience",      # 2 factors
        "Implementation Time"   # No factors (direct scoring)
    ]

    criterion_weights = {
        "Cost Efficiency": 4,
        "User Experience": 5,
        "Implementation Time": 3
    }

    factors = {
        "Cost Efficiency": ["Hardware Costs", "Maintenance", "Scalability"],
        "User Experience": ["Learnability", "Satisfaction"],
        "Implementation Time": ["Implementation Time"]  # Single factor == direct scoring
    }

    factor_weights = {
        "Cost Efficiency": {
            "Hardware Costs": 5,
            "Maintenance":    3,
            "Scalability":    4
        },
        "User Experience": {
            "Learnability":   4,
            "Satisfaction":   5
        },
        "Implementation Time": {
            "Implementation Time": 1.0  # Auto-normalized to 1.0
        }
    }

    scores = {
        "System Alpha": {
            "Cost Efficiency": {
                "Hardware Costs": 4,
                "Maintenance":    3,
                "Scalability":    2
            },
            "User Experience": {
                "Learnability":   3,
                "Satisfaction":   4
            },
            "Implementation Time": {
                "Implementation Time": 5
            }
        },
        "System Beta": {
            "Cost Efficiency": {
                "Hardware Costs": 2,
                "Maintenance":    4,
                "Scalability":    5
            },
            "User Experience": {
                "Learnability":   5,
                "Satisfaction":   3
            },
            "Implementation Time": {
                "Implementation Time": 3
            }
        },
        "System Gamma": {
            "Cost Efficiency": {
                "Hardware Costs": 3,
                "Maintenance":    3,
                "Scalability":    4
            },
            "User Experience": {
                "Learnability":   4,
                "Satisfaction":   5
            },
            "Implementation Time": {
                "Implementation Time": 4
            }
        }
    }

    return options, criteria, criterion_weights, factors, factor_weights, scores

# This function gathers hardcoded values for options, criteria, criterion_weights, factors, 
# factor_weights, and scores.  Once they have been assigned, the gathered information is all returned.

def garfield_example():

    # Hardcoded values for Garfield example

    MIN_SCORE = 0 # reset for consistency with hardcoded scores
    MAX_SCORE = 5 # reset for consistency with hardcoded scores

    options = [
        "Sleep",
        "Eat cat food", 
        "Eat Jon's lasagne", 
        "Hassle Jon",
        "Prank Odie"
    ]
    
    criteria = ["Relieve tiredness", "Satisfy hunger", "Have fun", "Avoid retaliation/punishment"]
    
    criterion_weights = {
        "Relieve tiredness": 5,
        "Satisfy hunger": 5,
        "Have fun": 4,
        "Avoid retaliation/punishment": 3
    }
    
    factors = {
        "Relieve tiredness": ["Current tiredness", "Presence of Jon or Odie"],
        "Satisfy hunger": ["Current hunger level", "Availability of delicious food"],
        "Have fun": ["Presence of Jon or Odie", "Good idea what to do", "Hilarity of action"],
        "Avoid retaliation/punishment": ["Shouting danger", "Barking danger", "Biting danger", "Exclusion danger", "Starvation danger"]
    }
    
    factor_weights = {
        "Relieve tiredness": {"Current tiredness": 5, "Presence of Jon or Odie": 3},
        "Satisfy hunger": {"Current hunger level": 5, "Availability of delicious food": 4},
        "Have fun": {"Presence of Jon or Odie": 5, "Good idea what to do": 4, "Hilarity of action": 3},
        "Avoid retaliation/punishment": {"Shouting danger": 1, "Barking danger": 2, "Biting danger": 4, "Exclusion danger": 4, "Starvation danger": 5}
    }

    scores = {
        "Sleep": {
            "Relieve tiredness": {
                "Current tiredness":              2,
                "Presence of Jon or Odie":        0
                },
            "Satisfy hunger": {
                "Current hunger level":           0,
                "Availability of delicious food": 0
                },
            "Have fun": {
                "Presence of Jon or Odie":        0,
                "Good idea what to do":           0,
                "Hilarity of action":             0
                },
            "Avoid retaliation/punishment": {
                "Shouting danger":                4,
                "Barking danger":                 4,
                "Biting danger":                  3,
                "Exclusion danger":               5,
                "Starvation danger":              5
                }
            },
        "Eat cat food": {
            "Relieve tiredness": {
                "Current tiredness":              0,
                "Presence of Jon or Odie":        0
                },
            "Satisfy hunger": {
                "Current hunger level":           3,
                "Availability of delicious food": 1
                },
            "Have fun": {
                "Presence of Jon or Odie":        0,
                "Good idea what to do":           0,
                "Hilarity of action":             0
                },
            "Avoid retaliation/punishment": {
                "Shouting danger":                5,
                "Barking danger":                 5,
                "Biting danger":                  5,
                "Exclusion danger":               5,
                "Starvation danger":              5
                }
            },
        "Eat Jon's lasagne": {
            "Relieve tiredness": {
                "Current tiredness":              3,
                "Presence of Jon or Odie":        2
                },
            "Satisfy hunger": {
                "Current hunger level":           3,
                "Availability of delicious food": 5
                },
            "Have fun": {
                "Presence of Jon or Odie":        2,
                "Good idea what to do":           2,
                "Hilarity of action":             1
                },
            "Avoid retaliation/punishment": {
                "Shouting danger":                2,
                "Barking danger":                 4,
                "Biting danger":                  4,
                "Exclusion danger":               2,
                "Starvation danger":              1
                }
            },
        "Hassle Jon": {
            "Relieve tiredness": {
                "Current tiredness":              3,
                "Presence of Jon or Odie":        5
                },
            "Satisfy hunger": {
                "Current hunger level":           0,
                "Availability of delicious food": 2
                },
            "Have fun": {
                "Presence of Jon or Odie":        5,
                "Good idea what to do":           3,
                "Hilarity of action":             3
                },
            "Avoid retaliation/punishment": {
                "Shouting danger":                1,
                "Barking danger":                 4,
                "Biting danger":                  4,
                "Exclusion danger":               1,
                "Starvation danger":              1
                }
            },
        "Prank Odie": {
            "Relieve tiredness": {
                "Current tiredness":              3,
                "Presence of Jon or Odie":        5
                },
            "Satisfy hunger": {
                "Current hunger level":           0,
                "Availability of delicious food": 0
                },
            "Have fun": {
                "Presence of Jon or Odie":        5,
                "Good idea what to do":           5,
                "Hilarity of action":             5
                },
            "Avoid retaliation/punishment": {
                "Shouting danger":                3,
                "Barking danger":                 0,
                "Biting danger":                  1,
                "Exclusion danger":               2,
                "Starvation danger":              4
                }
            }
    }

    # Return all gathered information
    return options, criteria, criterion_weights, factors, factor_weights, scores

# This function prompts the user to enter multiple strings, one per line.
# Once a blank line is entered, the list of strings is returned.
  
def get_list(prompt):
    print(prompt)
    items = []
    while True:
        item = input()
        if item == "":
            break
        items.append(item)
    return items

# This function prompts the user to enter options, criteria, criterion_weights, factors, 
# and factor_weights.  Once it has been entered, the gathered information is all returned.

def get_user_input():
    print("""
             Specify options that you need to choose from,\n
             criteria you would use to decide the best option,\n
             and factors / components of criteria if needed.\n
          """)

    # Get options
    options = get_list("Enter your options, one per line. Press Enter on a blank line to finish:")

    # Get criteria
    criteria = get_list("\nEnter decision criteria, one per line. Press Enter on a blank line to finish:")

    # Get weights for each criterion
    criterion_weights = {}
    print("\nAssign a weight to each criterion to reflect its overall importance:")
    for criterion in criteria:
        while True:
            try:
                value = float(input(f"\nEnter weight ({MIN_SCORE}-{MAX_SCORE}) for overall importance of'{criterion}': "))
                if MIN_SCORE <= value <= MAX_SCORE:
                    criterion_weights[criterion] = value
                    break
                else:
                    print(f"Please enter a number between {MIN_SCORE} and {MAX_SCORE}.")
            except ValueError:
                print(f"Please enter a valid number between {MIN_SCORE} and {MAX_SCORE}.")

    # Get factors for each criterion
    factors = {}
    for criterion in criteria:
        prompt = f"\nFor '{criterion}', press Enter again for direct scoring, or enter factors, one per line. Press Enter on a blank line to finish:"
        entered_factors = get_list(prompt)
        factors[criterion] = entered_factors if entered_factors else [criterion]  # Default to criterion name

    # Get weights for factor-criterion pairs
    factor_weights = {}
    for criterion in criteria:
        factor_weights[criterion] = {}
        if len(factors[criterion]) == 1 and factors[criterion][0] == criterion:
            # Auto-set weight to 1 if no factors
            factor_weights[criterion][criterion] = 1.0
        else:
            for factor in factors[criterion]:
                while True:
                    try:
                        value = float(input(
                            f"\nEnter weight ({MIN_SCORE}-{MAX_SCORE}) for importance of '{factor}' in '{criterion}': "))
                        if MIN_SCORE <= value <= MAX_SCORE:
                            factor_weights[criterion][factor] = value
                            break
                        else:
                            print(f"Please enter a number between {MIN_SCORE} and {MAX_SCORE}.")
                    except ValueError:
                            print(f"Please enter a valid number between {MIN_SCORE} and {MAX_SCORE}.")

    # Get scores for options in reference to criteria or factor-criterion pairs
    scores = {}
    print("\n=== Scoring Phase ===")
    for option in options:
        scores[option] = {}
        print(f"\nScoring '{option}':")
        for criterion in criteria:
            scores[option][criterion] = {}
            if len(factors[criterion]) == 1 and factors[criterion][0] == criterion:
                # Direct criterion scoring
                while True:
                    try:
                        score = float(input(
                            f"Score ({MIN_SCORE}-{MAX_SCORE}) for '{option}' considering '{criterion}': "))
                        if MIN_SCORE <= score <= MAX_SCORE:
                            scores[option][criterion][criterion] = score
                            break
                        else:
                            print(f"Please enter a number between {MIN_SCORE} and {MAX_SCORE}.")
                    except ValueError:
                        print(f"Please enter a valid number between {MIN_SCORE} and {MAX_SCORE}.")
            else:
                # Factor-based scoring
                for factor in factors[criterion]:
                    while True:
                        try:
                            score = float(input(
                                f"Score ({MIN_SCORE}-{MAX_SCORE}) for '{option}' considering '{factor}' ({criterion}): "))
                            if MIN_SCORE <= score <= MAX_SCORE:
                                scores[option][criterion][factor] = score
                                break
                            else:
                                print(f"Please enter a number between {MIN_SCORE} and {MAX_SCORE}.")
                        except ValueError:
                            print(f"Please enter a valid number between {MIN_SCORE} and {MAX_SCORE}.")

    # Return all gathered information
    return options, criteria, criterion_weights, factors, factor_weights, scores

# This function normalises a set of weights so that they add up to 1.

def normalize_weights(weights):
    total = sum(weights.values())
    return {key: value / total for key, value in weights.items()} if total > 0 else weights

# This function computes the option scores.

def calculate_weighted_scores(options, criteria, criterion_weights, factors, factor_weights, scores):

    # Sending the weights to be normalised first
    norm_criterion_weights = normalize_weights(criterion_weights)
    norm_factor_weights = {
        criterion: normalize_weights(factor_weights[criterion])
        for criterion in criteria
    }

    option_scores = {}
    for option in options:
        total_score = 0
        for criterion in criteria:
            criterion_score = 0
            if len(factors[criterion]) == 1 and factors[criterion][0] == criterion:
                # Direct criterion calculation
                score = scores[option][criterion][criterion]
                criterion_score = score  # No factor weighting
            else:
                # Factor-based calculation
                for factor in factors[criterion]:
                    score = scores[option][criterion][factor]
                    criterion_score += score * norm_factor_weights[criterion][factor]

            total_score += criterion_score * norm_criterion_weights[criterion]

        option_scores[option] = total_score
        
    return option_scores

# This function displays the final results.

from tabulate import tabulate

def display_results(option_scores, scores, criterion_weights, factor_weights):

    print("\n=== Decision Results ===")
    sorted_options = sorted(option_scores.items(), key=lambda x: x[1], reverse=True)
    for option, score in sorted_options:
        print(f"{option}: {score:.2f}")

    # Find all options with the maximum score (allowing for floating point tolerance)
    max_score = max(option_scores.values())
    TOLERANCE = 1e-8
    best_options = [option for option, score in option_scores.items() if abs(score - max_score) < TOLERANCE]

    if len(best_options) == 1:
        print(f"\nBest Option: {best_options[0]} with a score of {max_score:.2f}")
    else:
        print(f"\nBest Options (tie): {', '.join(best_options)} with a score of {max_score:.2f}")

    # Table 1: Raw Scores
    print("\n=== Raw Scores (Criteria -> Factors) ===")
    for option in scores:
        print(f"\nOption: {option}")
        rows = []
        for criterion in scores[option]:
            for factor in scores[option][criterion]:
                rows.append([criterion, factor, scores[option][criterion][factor]])
        print(tabulate(rows, headers=["Criterion", "Factor", "Score"], tablefmt="grid"))

    # Table 2: Normalized Criterion Weights
    print("\n=== Normalized Criterion Weights ===")
    total_criterion_weight = sum(criterion_weights.values())
    criterion_table = [[criterion, weight, weight / total_criterion_weight] for criterion, weight in criterion_weights.items()]
    print(tabulate(criterion_table, headers=["Criterion", "Raw Weight", "Normalized Weight"], tablefmt="grid"))

    # Table 3: Normalized Factor Weights per Criterion
    print("\n=== Normalized Factor Weights ===")
    for criterion, factors in factor_weights.items():
        print(f"\nCriterion: {criterion}")
        total = sum(factors.values())
        factor_table = [[factor, weight, weight / total] for factor, weight in factors.items()]
        print(tabulate(factor_table, headers=["Factor", "Raw Weight", "Normalized Weight"], tablefmt="grid"))

    # Table 4: Weighted Criterion Scores for each Option
    print("\n=== Weighted Criterion Scores ===")
    for option in scores:
        print(f"\nOption: {option}")
        rows = []
        for criterion in scores[option]:
            factor_score = sum(
                scores[option][criterion][factor] * factor_weights[criterion][factor] / sum(factor_weights[criterion].values())
                for factor in scores[option][criterion]
            )
            criterion_weight = criterion_weights[criterion] / total_criterion_weight
            weighted_score = factor_score * criterion_weight
            rows.append([criterion, f"{factor_score:.2f}", f"{weighted_score:.2f}"])
        print(tabulate(rows, headers=["Criterion", "Criterion Score", "Weighted Score"], tablefmt="grid"))

# This function saves the final results to a text file.

import io
from contextlib import redirect_stdout

def save_display_results_to_file(option_scores, scores, criterion_weights, factor_weights, filename="decision_results.txt"):
    buffer = io.StringIO()
    # Redirect all print output to the buffer
    with redirect_stdout(buffer):
        display_results(option_scores, scores, criterion_weights, factor_weights)
    # Write the buffer contents to the file
    with open(filename, "w", encoding="utf-8") as f:
        f.write(buffer.getvalue())

# This function detects if user input is possible in the environment

import sys

def input_available():
    try:
        return sys.stdin.isatty()
    except Exception:
        return False

# This is the main program.

def decision_making_tool():

    print("""
             Welcome to the Decision-Making Assistant!\n\n
          """)
    if input_available():    # prevents crash in environments where user input is not possible

        response = input("Do you need introductory instructions? (Press Enter for no or any other input for yes): ")
        if response.strip() != "":
            print_instructions()

        simple = input("Do you want to run the simple 2x2 example? (Press Enter for no or any other input for yes): ")
        if simple.strip() != "":
            options, criteria, criterion_weights, factors, factor_weights, scores = simple_2_by_2_example()
        else:
            mixed = input("Do you want to run the mixed factor example? (Press Enter for no or any other input for yes): ")
            if mixed.strip() != "":
                options, criteria, criterion_weights, factors, factor_weights, scores = mixed_factors_example()
            else:
                garfield = input("Do you want to run the Garfield example? (Press Enter for no or any other input for yes): ")
                if garfield.strip() != "":
                    options, criteria, criterion_weights, factors, factor_weights, scores = garfield_example()
                else:
                    options, criteria, criterion_weights, factors, factor_weights, scores = get_user_input()
    else:
        print("\nUser input not available in this environment. Printing instructions and defaulting to the Garfield example.\n")
        print_instructions()
        options, criteria, criterion_weights, factors, factor_weights, scores = garfield_example()

    option_scores = calculate_weighted_scores(options, criteria, criterion_weights, factors, factor_weights, scores)

    display_results(option_scores, scores, criterion_weights, factor_weights)

    save_display_results_to_file(option_scores, scores, criterion_weights, factor_weights)
    print("Results saved to decision_results.txt")

# Run the tool
decision_making_tool()
