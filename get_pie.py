import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Pie
# from pyecharts.faker import Faker

chart = pd.read_csv('KFC_province_number.csv')
province = list(chart['省份'])
numbers = list(chart['KFC总数'])
data = [list(z) for z in zip(province, numbers)]

c = (
    Pie(init_opts=opts.InitOpts(
        width='1920px',
        height='900px',
    ))
    .add(
        "",
        data,
        radius=["40%", "75%"],
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="全国KFC门店分布"),
        legend_opts=opts.LegendOpts(orient="vertical", pos_top="15%", pos_left="2%"),
        toolbox_opts=opts.ToolboxOpts(is_show=True,
                                      orient='vertical',
                                      feature={'saveAsImage': {'type_': 'jpeg', 'pixel_ration': 3}})
    )
    .set_series_opts(label_opts=opts.LabelOpts(is_show=True,formatter="{b}: {c}"))
    .render("pie_radius.html")
)
