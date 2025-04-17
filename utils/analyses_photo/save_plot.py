from quiz_module.models import Quiz
# import matplotlib.backends
import matplotlib
import seaborn as sns

sns.set()
matplotlib.use('agg')
# matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import matplotlib.dates as mpl_dates


def save_plot1(request, farsi, f_scores, f_len, riazi, r_scores, r_len,current_user):
    fig = plt.figure()

    ax2 = fig.add_subplot(3, 2, 2)
    ax2.plot(r_len + 1, r_scores, 'r-', marker='o')
    ax2.set_title("riazi", c='r')
    # plt.xlim(1, len(farsi)+1)
    # ax2.axis([1,len(riazi),0,5])
    ax2.set(xlabel='azmoon', ylabel='nomreh')
    plt.xticks(range(1, len(riazi) + 1))
    plt.yticks(range(0, 7))

    ax5 = fig.add_subplot(3, 2, 5)
    ax5.plot(f_len+1 , f_scores, 'b-', marker='o')
    ax5.set_title("farsi", c='b')
    # plt.xlim(1, len(farsi) )
    plt.xticks(range(1, len(farsi) + 1))
    plt.yticks(range(0, 7))
    ax5.set(xlabel='azmoon', ylabel='nomreh')

    plt.grid(True)
    fig.savefig(f"assets/images/analyses_photo/{current_user.id}_1.png", bbox_inches="tight")
    extent1 = ax5.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
    fig.savefig(f"assets/images/analyses_photo/{current_user.id}_2.png", format='png', bbox_inches=extent1.expanded(1.5, 2))
    extent2 = ax2.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
    fig.savefig(f"assets/images/analyses_photo/{current_user.id}_3.png", bbox_inches=extent2.expanded(1.4, 2))


def save_plot2(request, farsi, f_scores, f_len, riazi, r_scores, r_len,current_user):
    fig, ax = plt.subplots()
    ax.plot(f_len, f_scores, marker='o', label='farsi')
    ax.plot(r_len, r_scores, marker='o', label='riazi')
    # plt.plot(f_len, f_scores,'b-',r_len, r_scores,'r--',marker='o')
    # plt.xlim(1, max(len(farsi), len(riazi)))
    ax.set(xlabel='azmoon', ylabel='nomreh')
    ax.set_title("all quizes")
    plt.xticks(range(1, max(len(farsi), len(riazi))+1))
    plt.yticks(range(0, 7))
    ax.legend()
    plt.grid(True)
    plt.savefig(f"assets/images/analyses_photo/{current_user.id}_4.png")


def save_plot3(request, farsi_average, riazi_average,current_user):
    names = ['farsi', 'riazi']
    values = [farsi_average, riazi_average]
    plt.figure(figsize=(3, 3))
    plt.subplot(111)
    plt.bar(names, values)

    # plt.subplot(122)
    # plt.scatter(names, values)
    # plt.subplot(133)
    # plt.plot(names, values)
    plt.suptitle('lessons average', c='b')
    # plt.grid(True)
    plt.savefig(f"assets/images/analyses_photo/{current_user.id}_5.png", dpi=1500)
    plt.show()

# plt.plot(f_len, f_scores, 'r', r_len, r_scores, 'g')
# plt.xlim(1, max(len(farsi), len(riazi)))
