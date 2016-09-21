#!/usr/bin/env python

from pygal import Config
from pygal.maps.fr import Regions
from pygal.style import LightenStyle


config = Config()
config.css.append('inline: .background {fill: transparent !important}')

style = LightenStyle(
    '#62ad96', background='transparent', plot_background='#ddd',
    font_family='googlefont:PT Sans')

graph = Regions(
    config, show_legend=False, tooltip_fancy_mode=False, style=style,
    stroke_style={'width': 5})
graph.add('Rhône-Alpes', [{'value': 82, 'xlink': {
    'href': '/region-rhone-alpes/', 'target': '_top'}}])
svg = graph.render()

svg = svg.replace(b': 1<', b'<')
svg = svg.replace(b'Pygal', 'Sites en démonstration'.encode('utf-8'))

with open('static/images/map.svg', 'wb') as fb:
    fb.write(svg)
