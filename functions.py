def find_and_click(wait, ec, by, value):
    """Finds and clicks an element by provided method and its value"""
    try:
        element = wait.until(ec.element_to_be_clickable((by, value)))
        element.click()
    except Exception as e:
        print(f"Error clicking element {value}: {e}")


def input_data(wait, ec, by=None, value=None, element=None, data=None, *args):
    """Finds and inputs data to an element by provided method and its value,
    or directly inputs to an already found element; possible to provide args which
    are keys that will be pressed after inputting data."""
    try:
        if element:
            target_element = element
        else:
            target_element = wait.until(ec.element_to_be_clickable((by, value)))

        if args:
            target_element.send_keys(data, *args)
        else:
            target_element.send_keys(data)
    except Exception as e:
        print(f"Error clicking element {value}: {e}")


