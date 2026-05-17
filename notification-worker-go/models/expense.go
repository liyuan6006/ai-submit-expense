package models

type Expense struct {
	EmployeeID string  `json:"employee_id"`
	Merchant   string  `json:"merchant"`
	Amount     float64 `json:"amount"`
	Category   string  `json:"category"`
}