import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Geo
# from pyecharts.faker import Faker

# 读取csv
chart = pd.read_csv('KFC_province_number.csv')
province = list(chart['省份'])
numbers = list(chart['KFC总数'])
data = [list(z) for z in zip(province, numbers)]
# test_data = [list(z) for z in zip(Faker.provinces, Faker.values())]
# print(data)

# 使用 pyecharts 库进行画图
c = (
    Geo(init_opts=opts.InitOpts(
        width='1920px',
        height='1080px',
    ))
    .add_schema(maptype="china")
    .add("KFC门店数量", data)
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(
        visualmap_opts=opts.VisualMapOpts(max_=977),
        title_opts=opts.TitleOpts(title="全国KFC门店分布"),
        toolbox_opts=opts.ToolboxOpts(is_show=True,
                                      orient='vertical',
                                      feature={'saveAsImage': {'type_': 'jpeg', 'pixel_ration': 3}})
    )
    .set_series_opts(
        label_opts=opts.LabelOpts(is_show=True, formatter='{b}', font_size=15, font_weight='Bold')
    )
    .render("geo_base.html")
)
