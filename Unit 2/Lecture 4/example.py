"""PyLab example."""

import pylab as plt


def retire(monthly, rate, terms):
    """Compound interest."""
    savings = [0]
    base = [0]
    m_rate = rate/12
    for i in range(terms):
        base += [i]
        savings += [savings[-1] * (1 + m_rate) + monthly]
    return base, savings


def display_retire_with_monthlies(monthlies, rate, terms):
    """Display retire by modifying monthly income."""
    plt.figure('retire_month')
    plt.clf()
    for monthly in monthlies:
        xvals, yvals = retire(monthly, rate, terms)
        plt.plot(
            xvals,
            yvals,
            label='retire: ' + str(monthly)
        )
        plt.legend(loc='upper left')


def display_retire_with_rates(month, rates, terms):
    """Display retire by modifying rates."""
    plt.figure('retire_rate')
    plt.clf()
    for rate in rates:
        xvals, yvals = retire(month, rate, terms)
        plt.plot(
            xvals,
            yvals,
            label='retire: ' + str(month) + ' : ' + str(int(rate*100))
        )
        plt.legend(loc='upper left')


def display_retire_with_monthlies_and_rates(monthlies, rates, terms):
    """Display both."""
    plt.figure('retire_both')
    plt.clf()
    plt.xlim(30*12, 40*12)
    month_labels = ['r', 'b', 'g', 'k']
    rate_labels = ['-', 'o' '--']
    for i in range(len(monthlies)):
        monthly = monthlies[i]
        month_label = month_labels[i % len(month_labels)]
        for j in range(len(rates)):
            rate = rates[j]
            rate_label = rate_labels[j % len(rate_labels)]
            xvals, yvals = retire(monthly, rate, terms)
            plt.plot(
                xvals,
                yvals,
                month_label + rate_label,
                label='retire: ' + str(monthly) + ' : ' + str(int(rate*100))
            )
            plt.legend(loc='upper left')


display_retire_with_monthlies(
    list(range(500, 1101, 100)),
    .05,
    40*12
)

display_retire_with_rates(
    800,
    [.03, .05, .07],
    40*12
)

display_retire_with_monthlies_and_rates(
    [500, 700, 900, 1100],
    [.03, .05, .07],
    40*12
)
