package consumers

import (
	"encoding/json"
	"log"

	"github.com/IBM/sarama"

	"notification-worker-go/models"
	"notification-worker-go/services"
)

type ExpenseConsumer struct {
}

func (c *ExpenseConsumer) Setup(
	session sarama.ConsumerGroupSession,
) error {

	return nil
}

func (c *ExpenseConsumer) Cleanup(
	session sarama.ConsumerGroupSession,
) error {

	return nil
}

func (c *ExpenseConsumer) ConsumeClaim(
	session sarama.ConsumerGroupSession,
	claim sarama.ConsumerGroupClaim,
) error {

	for message := range claim.Messages() {

		var expense models.Expense

		err := json.Unmarshal(
			message.Value,
			&expense,
		)

		if err != nil {

			log.Println(
				"JSON parse error:",
				err,
			)

			continue
		}

		log.Println(
			"Expense received:",
			expense,
		)

		services.SendNotification(
			expense,
		)

		session.MarkMessage(
			message,
			"",
		)
	}

	return nil
}
