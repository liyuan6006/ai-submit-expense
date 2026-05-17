package services

import (
	"fmt"

	"notification-worker-go/models"
)

func SendNotification(
	expense models.Expense,
) {

	fmt.Println("================================")
	fmt.Println("NOTIFICATION SENT")
	fmt.Println("Employee:", expense.EmployeeID)
	fmt.Println("Merchant:", expense.Merchant)
	fmt.Println("Amount:", expense.Amount)
	fmt.Println("Category:", expense.Category)
	fmt.Println("================================")
}
