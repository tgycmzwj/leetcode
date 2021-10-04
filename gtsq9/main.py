# Implement these functions as specified in the description.
# Add any additional functions/classes and import standard modules as you see fit.
order_book = {}
stock_orderid_mapping = {}


def on_new_order(order_id, stock_ticker, price, quantity, side):
    # since orderid is strictly increasing unique, no need to worry repeat
    if order_id not in order_book.keys():
        order_book[order_id] = [price, quantity, side]

    # associate stock with order
    if stock_ticker not in stock_orderid_mapping.keys():
        stock_orderid_mapping[stock_ticker] = [order_id]
    else:
        stock_orderid_mapping[stock_ticker].append(order_id)


def on_cancelled_order(order_id, quantity_to_cancel):
    # assume never cancel order_id that does not exist
    order_book[order_id] = [order_book[order_id][0], order_book[order_id][1] - quantity_to_cancel,
                            order_book[order_id][2]]
    # not quite clear but even those ids with 0 active shares are still kept in the book


def on_executed_order(order_id, quantity_executed):
    order_book[order_id] = [order_book[order_id][0], order_book[order_id][1] - quantity_executed,
                            order_book[order_id][2]]


# Return format:
# - List of price levels (list)
#   - Price level (tuple)
#     - Price (float)
#     - Total quantity (int)
#     - List of order IDs (list of ints)
def top(n, stock_ticker, side):
    # price,quantity,order_id
    all_orders = {}
    order_ids = stock_orderid_mapping[stock_ticker]
    for order_id in order_ids:
        b_price, b_quantity, b_side = order_book[order_id]
        if b_side == side:
            if b_price in all_orders.keys():
                all_orders[b_price] = [all_orders[b_price][0] + b_quantity, all_orders[b_price][1] + [order_id]]
            else:
                all_orders[b_price] = [b_quantity, [order_id]]
    for key, val in all_orders.items():
        if val[0] == 0:
            del all_orders[key]
    all_orders = list(all_orders.items())
    # remove orders with 0 quantity---I do not understand why this does not work...
    # all_orders=[item or item in all_orders if item[1][0]!=0]
    # sort

    all_orders = sorted(all_orders, key=lambda x: x[0])
    new_all_orders = []
    for item in all_orders:
        cur_ele = [item[0], item[1][0]]
        for sub_item in item[1][1]:
            cur_ele.append(sub_item)
        new_all_orders.append(cur_ele.copy())
    if side == 1:
        if n <= len(all_orders):
            return new_all_orders[::-1][:n]
        else:
            # not enough orders, just return the last one
            print('we do not have n price levels, the last one is returned')
            return new_all_orders[::-1]
    if side == -1:
        if n < len(all_orders):
            return new_all_orders[:n]
        else:
            print('we do not have n price levels, the last one is returned')
            return new_all_orders
    # there is a problem in the main part that I cannot modify. when we query the top n buy/sell from the order book, my program will naturally return a list, but the main part is not able to iterate over this list, instead it mechanically treat the first/second/remaining elements as price/quantity/associated orderids...I do not think there is a way to format the output in the desired format without changing the main program, especially given that explicitly check the length of the top_levels, for example, in Test case 1, the first query, length of top levels is 2, then it is impossible to unfold it into price/quantity/associated orderids


# Translate between stdin/out and function calls
def main():
    num_events = int(input())
    for _ in range(num_events):
        items = input().split(',')
        event_type, *items = items

        if event_type == 'N':
            order_id, stock_ticker, price, quantity, side = items
            order_id = int(order_id)
            price = float(price)
            quantity = int(quantity)
            side = int(side)
            on_new_order(order_id, stock_ticker, price, quantity, side)
        elif event_type == 'T':
            n, stock_ticker, side = items
            n = int(n)
            side = int(side)
            top_levels = top(n, stock_ticker, side)

            print(len(top_levels))
            for price, quantity, order_ids in top_levels:
                print(price, quantity, *order_ids, sep=',')
        else:
            order_id, quantity = items
            order_id = int(order_id)
            quantity = int(quantity)
            if event_type == 'C':
                on_cancelled_order(order_id, quantity)
            else:
                on_executed_order(order_id, quantity)


if __name__ == '__main__':
    main()
