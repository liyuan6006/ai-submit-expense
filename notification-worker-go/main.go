package main

import (
	"context"
	"log"

	"github.com/IBM/sarama"

	"notification-worker-go/consumers"
)

func main() {

	config := sarama.NewConfig()

	config.Version = sarama.V2_8_0_0

	config.Consumer.Group.Rebalance.Strategy =
		sarama.NewBalanceStrategyRoundRobin()

	config.Consumer.Offsets.Initial =
		sarama.OffsetNewest

	brokers := []string{
		"localhost:9092",
	}

	groupID := "notification-group"

	topics := []string{
		"expense-created",
	}

	consumerGroup, err :=
		sarama.NewConsumerGroup(
			brokers,
			groupID,
			config,
		)

	if err != nil {

		log.Fatal(err)
	}

	consumer := &consumers.ExpenseConsumer{}

	for {

		err := consumerGroup.Consume(
			context.Background(),
			topics,
			consumer,
		)

		if err != nil {

			log.Println(
				"Consume error:",
				err,
			)
		}
	}
}
