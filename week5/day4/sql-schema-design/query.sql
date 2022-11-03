

SELECT * FROM orders
    join order_menu_items on orders.id = order_menu_items.order_id
    join menu_items on order_menu_items.menu_item_id = menu_items.id;
    

SELECT * FROM orders
    left join order_menu_items on orders.id = order_menu_items.order_id
    