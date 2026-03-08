from  plotly.graph_objs._figure import Figure
import plotly.express as px
def apply_figure_layout( fig : Figure, title_text = '', xlabel_text = '', ylabel_text = '' ) -> Figure :
    
    xlabel_text = fig.layout.xaxis.title.text if xlabel_text == '' else xlabel_text
    ylabel_text = fig.layout.yaxis.title.text if ylabel_text == '' else ylabel_text
    title_text = fig.layout.title.text if title_text == '' else title_text  
    
    fig.update_traces(textfont_size=30)
    
    fig.update_layout(
        
        title = dict(
            pad = dict( l = 100 ), x = 0,
            text = title_text,
            font = dict( family = 'times', size = 25, color = "#0F52BA" )
        ),
        
        xaxis = dict(
            title = dict(
                text = xlabel_text, font = dict( family = 'times', size = 40, color = '#0F52BA' )
            ),
        tickfont =dict( family = 'times', size = 22, color = '#0F52BA' ),
        

        ),    
        yaxis = dict(
            title = dict(
                text = ylabel_text, font = dict( family = 'times', size = 40, color = '#0F52BA' )
            ),
        tickfont =dict( family = 'times', size = 22, color = "#0F52BA" )

        ),
        
        legend = dict(
            title = dict( font = dict( family = 'times', size = 30, color = "#0F52BA" ) ),
            bordercolor = "#0F52BA",
            font = dict( family = 'times', size = 27, color = '#0F52BA', lineposition = 'under' ),
            x = 1, y = 4
        ),
        
        
        hoverlabel = dict(
            font = dict( family = 'times', size = 23.5, color = '#0F52BA', lineposition = 'under' )
        ),
        
    )  
    
    fig.update_traces(
    textfont=dict(
        family="times", 
        size=28,
        )
    )
    
    return fig

ICE_BLUE = '#D6E6F3'
POWDER_BLUE = '#A6C5D7'
SAPPHIRE = '#0F52BA'
DEEP_NAVY = '#000926'    
    
BLUES_CLR_PALETTE = [ ICE_BLUE, POWDER_BLUE, SAPPHIRE, DEEP_NAVY  ]