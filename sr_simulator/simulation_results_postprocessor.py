
class simulation_results_postprocessor:
    def __init__(self, results_dict):
        self.results_dict = results_dict

    def reorient_results_for_each_partner(self):
        reorient_dict = {}
        click_savings_list = []
        sale_losses_list = []
        profit_losses_list = []
        profit_gain_list = []
        for partner in self.results_dict:
            reorient_dict[partner] = {}
            many_days_list = self.results_dict[partner]
            for day_dict in many_days_list:
                click_savings_list.append(day_dict['click_savings'])
                sale_losses_list.append(day_dict['sale_losses'])
                profit_losses_list.append(day_dict['profit_losses'])
                profit_gain_list.append(day_dict['profit_gain'])
            reorient_dict[partner]['click_savings'] = click_savings_list
            reorient_dict[partner]['sale_losses'] = sale_losses_list
            reorient_dict[partner]['profit_losses'] = profit_losses_list
            reorient_dict[partner]['profit_gain'] = profit_gain_list
        return reorient_dict

    def aggregate_results_for_each_partner(self, reoriented_dict):
        aggregated_dict = {}
        for partner in reoriented_dict:
            aggregated_dict[partner] = {}
            aggregated_value = 0
            for value in reoriented_dict[partner]['click_savings']:
                aggregated_value += value
            aggregated_dict[partner]['click_savings'] = aggregated_value
            aggregated_value = 0
            for value in reoriented_dict[partner]['sale_losses']:
                aggregated_value += value
            aggregated_dict[partner]['sale_losses'] = aggregated_value
            aggregated_value = 0
            for value in reoriented_dict[partner]['profit_losses']:
                aggregated_value += value
            aggregated_dict[partner]['profit_losses'] = aggregated_value
            aggregated_value = 0
            for value in reoriented_dict[partner]['profit_gain']:
                aggregated_value += value
            aggregated_dict[partner]['profit_gain'] = aggregated_value
        return aggregated_dict

    def aggregate_results_for_all_partners(self, aggregated_for_each_dict):
        aggregated_for_all_dict = {}
        aggregated_clicks = []
        aggregated_sales = []
        aggregated_profit_losses = []
        aggregated_profit_gain = []
        for partner in aggregated_for_each_dict:
            aggregated_clicks.append(aggregated_for_each_dict[partner]['click_savings'])
            aggregated_sales.append(aggregated_for_each_dict[partner]['sale_losses'])
            aggregated_profit_losses.append(aggregated_for_each_dict[partner]['profit_losses'])
            aggregated_profit_gain.append(aggregated_for_each_dict[partner]['profit_gain'])
        aggregated_for_all_dict['click_savings'] = aggregated_clicks
        aggregated_for_all_dict['sale_losses'] = aggregated_sales
        aggregated_for_all_dict['profit_losses'] = aggregated_profit_losses
        aggregated_for_all_dict['profit_gain'] = aggregated_profit_gain
        return aggregated_for_all_dict

    def sum_results_for_all_partners(self, aggregated_dict):
        summed_dict = {}
        summed_clicks = 0.0
        summed_sales = 0.0
        summed_profit_losses = 0.0
        summed_profit_gain = 0.0
        for value in aggregated_dict['click_savings']:
            summed_clicks += value
        for value in aggregated_dict['sale_losses']:
            summed_sales += value
        for value in aggregated_dict['profit_losses']:
            summed_profit_losses += value
        for value in aggregated_dict['profit_gain']:
            summed_profit_gain += value
        summed_dict['click_savings'] = summed_clicks
        summed_dict['sale_losses'] = summed_sales
        summed_dict['profit_losses'] = summed_profit_losses
        summed_dict['profit_gain'] = summed_profit_gain
        return summed_dict