import { Module } from '@nestjs/common';

import { HttpModule } from '@nestjs/axios';

import { ExpenseController }
from './expense.controller';

import { ExpenseService }
from './expense.service';

@Module({

    imports: [
        HttpModule
    ],

    controllers: [
        ExpenseController
    ],

    providers: [
        ExpenseService
    ]
})
export class ExpenseModule {}