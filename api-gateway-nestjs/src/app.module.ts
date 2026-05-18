import { Module } from '@nestjs/common';

import { ExpenseModule }
from './expense/expense.module';

@Module({

    imports: [
        ExpenseModule
    ]
})
export class AppModule {}
