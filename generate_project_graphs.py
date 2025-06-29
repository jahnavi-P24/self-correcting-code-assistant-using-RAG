import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load results
def load_results(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
    return data

def flatten_results(results, dataset='mbpp'):
    rows = []
    for entry in results:
        if dataset == 'mbpp':
            res = entry['result']
            exec_res = res.get('execution_result', {})
            rows.append({
                'task_id': entry.get('task_id'),
                'description': entry.get('description'),
                'exit_code': exec_res.get('exit_code'),
                'stderr': exec_res.get('stderr'),
                'stdout': exec_res.get('stdout'),
                'execution_time': exec_res.get('execution_time'),
                'processing_time': res.get('processing_time'),
                'errors': res.get('errors'),
                'suggestions': res.get('suggestions'),
                'hints': res.get('hints'),
                'warnings': res.get('warnings'),
                'elapsed': entry.get('time'),
            })
        else:
            res = entry['result']
            exec_res = res.get('execution_result', {})
            rows.append({
                'id': entry.get('id'),
                'exit_code': exec_res.get('exit_code'),
                'stderr': exec_res.get('stderr'),
                'stdout': exec_res.get('stdout'),
                'execution_time': exec_res.get('execution_time'),
                'processing_time': res.get('processing_time'),
                'errors': res.get('errors'),
                'suggestions': res.get('suggestions'),
                'hints': res.get('hints'),
                'warnings': res.get('warnings'),
                'elapsed': entry.get('elapsed'),
            })
    return pd.DataFrame(rows)

def plot_success_rate(df, name):
    success = (df['exit_code'] == 0).sum()
    fail = (df['exit_code'] != 0).sum()
    plt.figure(figsize=(5,5))
    plt.pie([success, fail], labels=['Success', 'Fail'], autopct='%1.1f%%', colors=['#4CAF50', '#F44336'])
    plt.title(f'Code Execution Success Rate ({name})')
    plt.savefig(f'{name}_success_rate.png')
    plt.close()

def plot_error_types(df, name):
    error_types = df['errors'].dropna().apply(lambda x: str(x).split(':')[0] if isinstance(x, str) else 'Other')
    if error_types.empty:
        print(f"[SKIP] No error types to plot for {name}.")
        return
    plt.figure(figsize=(7,5))
    error_types.value_counts().plot(kind='bar', color='#F44336')
    plt.title(f'Error Type Distribution ({name})')
    plt.xlabel('Error Type')
    plt.ylabel('Count')
    plt.tight_layout()
    plt.savefig(f'{name}_error_types.png')
    plt.close()

def plot_execution_time(df, name):
    plt.figure(figsize=(7,5))
    sns.histplot(df['execution_time'].dropna(), bins=30, kde=True, color='#2196F3')
    plt.title(f'Execution Time Distribution ({name})')
    plt.xlabel('Execution Time (s)')
    plt.ylabel('Frequency')
    plt.tight_layout()
    plt.savefig(f'{name}_execution_time.png')
    plt.close()

def plot_ai_feature_coverage(df, name):
    features = ['errors', 'suggestions', 'hints', 'warnings']
    counts = [df[f].notnull().sum() for f in features]
    plt.figure(figsize=(7,5))
    sns.barplot(x=features, y=counts, palette='Set2')
    plt.title(f'AI Feature Coverage ({name})')
    plt.ylabel('Count')
    plt.tight_layout()
    plt.savefig(f'{name}_ai_feature_coverage.png')
    plt.close()

def main():
    os.makedirs('project_graphs', exist_ok=True)
    os.chdir('project_graphs')
    # MBPP
    mbpp = load_results('../mbpp_results.json')
    mbpp_df = flatten_results(mbpp, dataset='mbpp')
    plot_success_rate(mbpp_df, 'mbpp')
    plot_error_types(mbpp_df, 'mbpp')
    plot_execution_time(mbpp_df, 'mbpp')
    plot_ai_feature_coverage(mbpp_df, 'mbpp')
    # BigCode
    bigcode = load_results('../bigcode_results.json')
    bigcode_df = flatten_results(bigcode, dataset='bigcode')
    plot_success_rate(bigcode_df, 'bigcode')
    plot_error_types(bigcode_df, 'bigcode')
    plot_execution_time(bigcode_df, 'bigcode')
    plot_ai_feature_coverage(bigcode_df, 'bigcode')
    print('Graphs generated in project_graphs/')

if __name__ == '__main__':
    main() 