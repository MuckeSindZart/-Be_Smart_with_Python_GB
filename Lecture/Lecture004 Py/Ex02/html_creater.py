from user_interface import temperature_view
from user_interface import pressure_view
from user_interface import wind_speed_view


def create(device=1):
    style = f'style="font-size:22px;"'
    html = f'<html>\n <head></head>\n <body>\n'
    html += f'    <p {style}> Temperature: {temperature_view(device)} c</p>\n'
    html += f'    <p {style}> Pressure: {pressure_view(device)} m/s</p>\n'
    html += f'    <p {style}> Wind_speed: {wind_speed_view(device)} mmHg</p>\n'
    html += f'</body>\n</html>'

    with open('index.html', 'w') as page:
        page.write(html)

    return html


def new_create(data, device=1):
    t, p, w = data
    t = t * 1.8 + 32
    style = f'style="font-size:22px;"'
    html = f'<html>\n <head></head>\n <body>\n'
    html += f'    <p {style}> Temperature: {t} f</p>\n'
    html += f'    <p {style}> Pressure: {p} m/s</p>\n'
    html += f'    <p {style}> Wind_speed: {w} mmHg</p>\n'
    html += f'</body>\n</html>'

    with open('new_index.html', 'w') as page:
        page.write(html)

    return data
