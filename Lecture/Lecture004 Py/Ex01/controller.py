import model_sub
import view

def button_click():
    value_a = view.get_value()
    value_b = view.get_value()
    model_sub.init(value_a, value_b)
    result = model_sub.do_it()
    view.view_data(result,'result')