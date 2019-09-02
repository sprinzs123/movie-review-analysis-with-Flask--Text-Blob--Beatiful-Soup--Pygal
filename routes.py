from flask import Flask, render_template, request, url_for, redirect, flash
import critic_reviews as scripts
import stats_builder as make_data
import pygal

app = Flask(__name__)
app.secret_key = "qwerty"


@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/results', methods=('POST',))
def results():
    # use try to get flash message when we encountered error and redirect to home page
    # 1st if statement insures that we use full url in for data scrapind otherwise we would get error
    # the output of our analyzer is a list with all variables we need
    # scripts.get_all_reviews(url)[x] where url is url we suply, and x the possition
    # positive=[0], negative=[1], objective=[2], subjective=[3], polarity scrores=[4], subjectivity scores=[5]
    try:
        url = request.form.get('url')
        polarity_list = scripts.get_all_reviews(url)[4]
        subjectivity_list = scripts.get_all_reviews(url)[5]

# get basic statistics about the scores
        pol_avg = make_data.get_average(polarity_list)
        subj_avg = make_data.get_average(subjectivity_list)
        pol_std = make_data.get_deviation(polarity_list)
        subj_pol = make_data.get_deviation(subjectivity_list)
#make graphs using pygal lirary

        graph = pygal.Bar(height=400, width=600, y_title='Repetitions', x_title="Scores", show_legend=False, xrange=(-1, 1))
        graph.title = 'All Polarity Scores'
        graph.x_labels = (make_data.polar_rounded_dictionary(polarity_list).keys())
        graph.add('Polarity', make_data.polar_rounded_dictionary(polarity_list).values())
        graph_data = graph.render_data_uri()

        graph2 = pygal.Bar(height=400, width=600, y_title='Repetitions', x_title="Scores", show_legend=False, xrange=(0, 1))
        graph2.title = 'All Subjectivity Scores'
        graph2.x_labels = (make_data.polar_rounded_dictionary(subjectivity_list).keys())
        graph2.add('Subjectivity', make_data.polar_rounded_dictionary(subjectivity_list).values())
        graph_data2 = graph2.render_data_uri()

        return render_template('result.html',
                                       positive=scripts.get_all_reviews(url)[0],
                                       negative=scripts.get_all_reviews(url)[1],
                                       objective=scripts.get_all_reviews(url)[2],
                                       subjective=scripts.get_all_reviews(url)[3],
                                       graph_data=graph_data, graph_data2=graph_data2,
                                       pol_avg=pol_avg, subj_avg=subj_avg,
                                       pol_std=pol_std, subj_pol=subj_pol)
    except:
        flash('Invalid url or no reviews found')
        return redirect(url_for('home'))



if __name__ == "__main__":
    app.run(debug=True)
#
# def results():
#     try:
#         url = request.form.get('url')
#         return render_template('result.html',
#                            positive=script.get_all_reviews(url)[0],
#                            negative=script.get_all_reviews(url)[1],
#                            objective=script.get_all_reviews(url)[2],
#                            subjective=script.get_all_reviews(url))
#     except:
#         flash('Invalid url. Please fix and resubmit.')
#         return redirect(url_for('home'))

    # graph = pygal.Bar()
    # graph.title = 'All Polarity Scores'
    # graph.x_labels = (make_data.polar_rounded_dictionary(polarity_list).keys())
    # graph.add('Polarity', make_data.polar_rounded_dictionary(polarity_list).values())
    # graph_data = graph.render_data_uri()
    #
    # graph2 = pygal.Bar()
    # graph2.title = 'All Polarity Scores'
    # graph2.x_labels = (make_data.polar_rounded_dictionary(subjectivity_list).keys())
    # graph2.add('Polarity', make_data.polar_rounded_dictionary(polarity_list).values())
    # graph_data2 = graph2.render_data_uri()
