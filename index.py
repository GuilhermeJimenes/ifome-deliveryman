if __name__ == '__main__':
    from src.application.delivery_app import DeliveryApp
    print('Waiting for a message...')

    while True:
        result = DeliveryApp().delivery()
        if result == 'error':
            break
        elif result:
            print("Result:", result)
