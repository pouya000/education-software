from django.shortcuts import render
# from django.views.generic import ListView
from account_module.models import User
from quiz_module.models import Quiz
import numpy as np
from utils.analyses_photo.save_plot import save_plot1, save_plot2, save_plot3
from utils.calculate_average import calc_avg


def student_analysis(request):
    current_user = User.objects.filter(id=request.user.id).first()
    quiz_farsi = Quiz.objects.filter(student_id=current_user.id, quizdetail__lesson=2)
    quiz_riazi = Quiz.objects.filter(student_id=current_user.id, quizdetail__lesson=1)
    farsi_average, riazi_average, riazi_scores, farsi_scores = calc_avg(quiz_farsi, quiz_riazi)
    quiz_farsi_len = np.arange(len(quiz_farsi))
    quiz_riazi_len = np.arange(len(quiz_riazi))
    save_plot1(request, quiz_farsi, farsi_scores, quiz_farsi_len, quiz_riazi, riazi_scores, quiz_riazi_len,
               current_user)
    save_plot2(request, quiz_farsi, farsi_scores, quiz_farsi_len, quiz_riazi, riazi_scores, quiz_riazi_len,
               current_user)
    save_plot3(request, farsi_average, riazi_average, current_user)
    context = {
        'current_user': current_user,
        # 'number_quiz_farsi': quiz_farsi_len,
        # 'number_quiz_riazi': quiz_riazi_len,
        # 'farsi_average': farsi_average_mark,
        # 'riazi_average': riazi_average_mark
    }
    return render(request, 'students_analysis_module/student_analysis_page.html', context)









    # print('farsi_average is: ', farsi_average, 'quiz_ririazi_averageazi is: ', riazi_average)
    # fig, axs = plt.subplots(2, 2)
    # axs[0, 0].plot(quiz_farsi_len, farsi_scores)
    # axs[0, 0].set_title("farsi")
    # axs[1, 0].plot(quiz_riazi_len, riazi_scores)
    # axs[1, 0].set_title("riazi")
    # axs[0, 1].plot([0,0], [0,0])
    # axs[0, 1].set_title("oloom")
    # axs[1, 1].plot(quiz_riazi_len, riazi_scores)
    # axs[1, 1].set_title("all lessons")
    # fig.tight_layout()

    # for ax in axs.flat:
    #     ax.set(xlabel='tedad azmoon', ylabel='nomreh')
    # # Hide x labels and tick labels for top plots and y ticks for right plots.
    # for ax in axs.flat:
    #     ax.label_outer()
    # fig.savefig('full_figure.png')
    #
    # # Save just the portion _inside_ the second axis's boundaries
    # extent = ax2.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
    # fig.savefig('ax2_figure.png', bbox_inches=extent)
