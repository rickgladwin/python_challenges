# Assume you have access to a function toss_biased() which returns 0 or 1 with a
# probability that's not 50-50 (but also not 0-100 or 100-0). You do not know the
# bias of the coin.
# Write a function to simulate an unbiased coin toss.
import random


# If we know the bias, flip the coin a high number of times and count the results.
# If the tails result is greater than the tails bias, it's tails. Else heads.
# To find the bias, flip the coin a high number of times.
# Accuracy will depend on the "high number" used in each step.

# Is there a way to compress these two steps?

def toss_biased() -> str:
    bias = 0.75  # (0.5 corresponds to an unbiased coin flip)
    roll = random.random()
    if roll <= bias:
        return 'heads'
    else:
        return 'tails'


def toss_unbiased() -> str:
    # TODO: determine bias in toss_biased
    # TODO: perform toss_biased and account for bias
    pass
