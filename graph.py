from pyecharts import options as opts
from pyecharts.charts import Radar

c_schema = [
    {"name": "策划", "max": 100, "min": 0},
    {"name": "程序", "max": 100, "min": 0},
    {"name": "美术", "max": 100, "min": 0},
    {"name": "特效", "max": 100, "min": 0},
    {"name": "剧情", "max": 100, "min": 0},
    {"name": "音乐", "max": 100, "min": 0},
    {"name": "运营", "max": 100, "min": 0}
]

def render_graph(values):
    c = Radar()
    c.set_colors(["#4587E7"])
    c.add_schema(
        schema=c_schema,
        shape="circle",
        center=["50%", "50%"],
        radius="80%",
        angleaxis_opts=opts.AngleAxisOpts(
            min_=0,
            max_=360,
            is_clockwise=False,
            interval=5,
            axistick_opts=opts.AxisTickOpts(is_show=False),
            axislabel_opts=opts.LabelOpts(is_show=False),
            axisline_opts=opts.AxisLineOpts(is_show=False),
            splitline_opts=opts.SplitLineOpts(is_show=False),
        ),
        radiusaxis_opts=opts.RadiusAxisOpts(
            min_=-4,
            max_=4,
            interval=2,
            splitarea_opts=opts.SplitAreaOpts(
                is_show=True, areastyle_opts=opts.AreaStyleOpts(opacity=1)
            ),
        ),
        polar_opts=opts.PolarOpts(),
        splitarea_opt=opts.SplitAreaOpts(is_show=False),
        splitline_opt=opts.SplitLineOpts(is_show=False),
    )
    c.add(
        series_name="自我分析",
        data=[{"value":values}],
        areastyle_opts=opts.AreaStyleOpts(opacity=0.1),
        linestyle_opts=opts.LineStyleOpts(width=1),
    )
    return c
