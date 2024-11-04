def bayes_theorem (probability_a, probability_b, probability_b_given_a):
    """
    This function calculates the formula of Bayes Theorem, which is the probability of event A happening given that event B has happened.

    Args:
      probability_a: The probability of event A happening.
      probability_b: The probability of event B happening.
      probability_b_given_a: The probability of event B happening given that event A has happened.

    Returns:
      The probability of event A happening given that event B has happened.
    """
    return (probability_b_given_a * probability_a) / probability_b