from typing import List, Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# 1. Define Pydantic models for the request body schema
class OrderItem(BaseModel):
    product_name: str
    quantity: int
    price: float


class CreateOrderRequest(BaseModel):
    customer_name: str
    email: str
    delivery_address: str
    items: List[OrderItem]
    payment_method: str = "Credit Card"  # Optional with default value


# 2. Existing GET Route
@app.get("/recommendations_krdnatural")
def krdnatural():
    return {"message": "Welcome to KRD Natural!"}


# 3. POST Route to process an E-Commerce Order
@app.post("/create_order")
def create_order(order: CreateOrderRequest):
    # Calculate order total
    total_amount = sum(item.quantity * item.price for item in order.items)

    # Return confirmation response
    return {
        "status": "Order Placed Successfully",
        "order_id": 1001,
        "customer": order.customer_name,
        "items_ordered": len(order.items),
        "total_amount": total_amount,
        "details": order,
    }

