import asyncio

class GetCancelOrders():
	"""
	Return the demo cancel orders json data for testing
	"""
	async def Orders():
		await asyncio.sleep(2)
		orders = [
			{
			    "id": 1073459966,
			    "admin_graphql_api_id": "",
			    "app_id": 755357713,
			    "browser_ip": "null",
			    "buyer_accepts_marketing": "false",
			    "cancel_reason": "null",
			    "cancelled_at": "null",
			    "cart_token": "null",
			    "checkout_id": "null",
		    },
		    {
			    "id": 1073459966,
			    "admin_graphql_api_id": "",
			    "app_id": 755357713,
			    "browser_ip": "null",
			    "buyer_accepts_marketing": "false",
			    "cancel_reason": "null",
			    "cancelled_at": "null",
			    "cart_token": "null",
			    "checkout_id": "null",
		    }
		   ]
		return orders