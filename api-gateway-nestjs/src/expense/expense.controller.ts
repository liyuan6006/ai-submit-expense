import {

    Body,
    Controller,
    Post

} from '@nestjs/common';

import { ExpenseService } from './expense.service';

import { SubmitExpenseDto }
from './dto/submit-expense.dto';

@Controller('expense')
export class ExpenseController {

    constructor(
        private readonly expenseService: ExpenseService
    ) {}

    @Post('submit')
    async submitExpense(

        @Body()
        body: SubmitExpenseDto

    ) {

        return await this.expenseService.submitExpense(
            body
        );
    }
}