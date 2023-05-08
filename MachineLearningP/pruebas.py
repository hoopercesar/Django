# def home(request):
#     # print(columnas)
#     x_data = t
#     y_data = y0
#     plot_div = plot([Scatter(x=x_data, y=y_data,
#                         mode='lines', name='test',
#                         opacity=0.8, marker_color='green')],
#                output_type='div')


#     title = 'esto es un título'
#     return render(request, 'home.html', 
#                   context={
#                       'plot_div': plot_div, 
#                     #   'hola': x_pred[0], 
#                       'color': 'red',
#                       })


# comando para hacer gáficos multiples en un mismo gráfico

    # trace0 = go.Scatter(
    #     x = t,
    #     y = x0,
    #     mode = 'lines',
    #     name = 'Prob: 0'
    # )

    # trace_1 = go.Scatter(
    #     x = t,
    #     y = x_1,
    #     mode = 'lines',
    #     name = 'Prob: -1'
    # )

    # trace1 = go.Scatter(
    #     x = t,
    #     y = entropia,
    #     mode = 'lines',
    #     name = 'Prob: 1'
    # )

    # data = [trace0, trace_1, trace1]
    # layout = go.Layout(title='Probabilidades', height=500)
    # fig = go.Figure(data=data, layout=layout)
    
    # plot_div = plotly.offline.plot(fig, auto_open=False, output_type='div')
    
    # context = {'plot_div': plot_div}

    # return render(request, 'probs.html', context)


################

    # trace1 = go.Scatter(
    #     x=t,
    #     y=y1,
    #     mode='lines',
    #     name='CCI 5'
    # )
    
    # trace2 = go.Scatter(
    #     x=t,
    #     y=y2,
    #     mode='lines',
    #     name='CCI 30'
    # )

    # trace3 = go.Scatter(
    #     x = t,
    #     y = 200*x_pred,
    #     mode = 'lines',
    #     name = 'Classificación'
    # )
    
    # data = [trace1, trace2, trace3]
    # layout = go.Layout(title='CCI', height=500)
    # fig = go.Figure(data=data, layout=layout)
    
    # plot_div = plotly.offline.plot(fig, auto_open=False, output_type='div')
    
    # context = {'plot_div': plot_div}
    
    # return render(request, 'base.html', context)

###################
 # print(columnas)
    # x_data = t
    # y_data = y0
    # plot_div = plot([Scatter(x=x_data, y=y_data,
    #                     mode='lines', name='test',
    #                     opacity=0.8, marker_color='green')],
    #            output_type='div')


    # title = 'esto es un título'
    # return render(request, 'home.html', 
    #               context={
    #                   'plot_div': plot_div, 
    #                 #   'hola': x_pred[0], 
    #                   'color': 'red',
    #                   })