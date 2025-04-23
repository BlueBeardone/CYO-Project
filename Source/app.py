from dash import Dash, dcc, html, Input, Output, State
import pandas as pd
import joblib
import os

# Load the trained Random Forest model
model_path = os.path.join(os.path.dirname(__file__), 'Test.pkl')
model = joblib.load(model_path)

app = Dash(__name__)
server = app.server

# Color scheme
colors = {
    'background': 'linear-gradient(195deg, #0A1A2F 0%, #1A2A4F 100%)',
    'card_bg': 'rgba(255, 255, 255, 0.05)',
    'accent': '#FF4B4B',
    'primary': '#0066CC',
    'text': '#FFFFFF',
    'input_bg': '#2A3A5F',
    'success': '#00C851',
    'border': '1px solid rgba(255, 255, 255, 0.1)'
}

app.layout = html.Div([
    html.Div([
        html.H1(
            "Production Predictor",
            style={
                'textAlign': 'center',
                'color': colors['text'],
                'fontFamily': 'Segoe UI, Arial',
                'padding': '30px',
                'marginBottom': '30px',
                'fontWeight': '700',
                'letterSpacing': '1.5px',
                'textShadow': '2px 2px 4px rgba(0,0,0,0.3)'
            }
        ),
        html.Div(
            [
                # Input Groups
                html.Div(
                    [
                        html.Label("Product Code", style={
                            'color': colors['text'],
                            'fontWeight': '600',
                            'marginBottom': '10px',
                            'display': 'block'
                        }),
                        dcc.Input(
                            id='Product_Code',
                            type='number',
                            value=16,
                            min=15,
                            max=18,
                            style={
                                'width': '100%',
                                'padding': '12px 18px',
                                'background': colors['input_bg'],
                                'border': colors['border'],
                                'borderRadius': '8px',
                                'color': colors['text'],
                                'fontSize': '15px'
                            }
                        )
                    ],
                    style={'marginBottom': '25px'}
                ),
                
                # Warehouse Input
                html.Div(
                    [
                        html.Label("Warehouse", style={
                            'color': colors['text'],
                            'fontWeight': '600',
                            'marginBottom': '10px',
                            'display': 'block'
                        }),
                        dcc.Input(
                            id='Warehouse',
                            type='text',
                            style={
                                'width': '100%',
                                'padding': '12px 18px',
                                'background': colors['input_bg'],
                                'border': colors['border'],
                                'borderRadius': '8px',
                                'color': colors['text'],
                                'fontSize': '15px'
                            }
                        )
                    ],
                    style={'marginBottom': '25px'}
                ),

                # Product Category Input
                html.Div(
                    [
                        html.Label("Product Category", style={
                            'color': colors['text'],
                            'fontWeight': '600',
                            'marginBottom': '10px',
                            'display': 'block'
                        }),
                        dcc.Input(
                            id='Product_Category',
                            type='text',
                            style={
                                'width': '100%',
                                'padding': '12px 18px',
                                'background': colors['input_bg'],
                                'border': colors['border'],
                                'borderRadius': '8px',
                                'color': colors['text'],
                                'fontSize': '15px'
                            }
                        )
                    ],
                    style={'marginBottom': '25px'}
                ),

                # Promotion Radio Items
                html.Div(
                    [
                        html.Label("Promotion", style={
                            'color': colors['text'],
                            'fontWeight': '600',
                            'marginBottom': '10px',
                            'display': 'block'
                        }),
                        dcc.RadioItems(
                            id='Promo',
                            options=[
                                {'label': ' Yes', 'value': 1, 'style': {'color': colors['text'], 'marginRight': '25px'}},
                                {'label': ' No', 'value': 0, 'style': {'color': colors['text']}}
                            ],
                            value=0,
                            inline=True,
                            style={'marginTop': '10px'}
                        )
                    ],
                    style={'marginBottom': '25px'}
                ),

                # Petrol Price Input
                html.Div(
                    [
                        html.Label("Petrol Price", style={
                            'color': colors['text'],
                            'fontWeight': '600',
                            'marginBottom': '10px',
                            'display': 'block'
                        }),
                        dcc.Input(
                            id='Petrol_price',
                            type='number',
                            value=5,
                            min=0,
                            max=20,
                            style={
                                'width': '100%',
                                'padding': '12px 18px',
                                'background': colors['input_bg'],
                                'border': colors['border'],
                                'borderRadius': '8px',
                                'color': colors['text'],
                                'fontSize': '15px'
                            }
                        )
                    ],
                    style={'marginBottom': '25px'}
                ),

                # High Demand Input
                html.Div(
                    [
                        html.Label("High Demand", style={
                            'color': colors['text'],
                            'fontWeight': '600',
                            'marginBottom': '10px',
                            'display': 'block'
                        }),
                        dcc.Input(
                            id='High_Demand',
                            type='number',
                            value=2,
                            min=0,
                            max=29,
                            style={
                                'width': '100%',
                                'padding': '12px 18px',
                                'background': colors['input_bg'],
                                'border': colors['border'],
                                'borderRadius': '8px',
                                'color': colors['text'],
                                'fontSize': '15px'
                            }
                        )
                    ],
                    style={'marginBottom': '30px'}
                ),

                # Submit Button
                html.Button(
                    'Calculate Production',
                    id='submit-button',
                    n_clicks=0,
                    style={
                        'width': '100%',
                        'padding': '16px',
                        'background': colors['primary'],
                        'color': colors['text'],
                        'border': 'none',
                        'borderRadius': '8px',
                        'fontSize': '16px',
                        'fontWeight': '600',
                        'cursor': 'pointer',
                        'transition': 'all 0.3s ease',
                        'marginTop': '20px',
                        ':hover': {
                            'background': '#004C99',
                            'transform': 'translateY(-1px)',
                            'boxShadow': '0 5px 15px rgba(0, 102, 204, 0.3)'
                        }
                    }
                )
            ],
            style={
                'background': colors['card_bg'],
                'padding': '40px',
                'borderRadius': '15px',
                'border': colors['border'],
                'boxShadow': '0 8px 32px rgba(0, 0, 0, 0.3)',
                'backdropFilter': 'blur(10px)',
                'maxWidth': '800px',
                'margin': '0 auto'
            }
        ),

        # Prediction Output
        html.Div(
            id='prediction-output',
            style={
                'background': colors['success'],
                'color': colors['text'],
                'padding': '20px',
                'borderRadius': '8px',
                'margin': '30px auto 0',
                'maxWidth': '400px',
                'textAlign': 'center',
                'fontSize': '18px',
                'fontWeight': '600',
                'boxShadow': '0 4px 15px rgba(0, 200, 81, 0.3)'
            }
        )
    ],
    style={
        'maxWidth': '1000px',
        'margin': '0 auto',
        'padding': '40px 20px'
    })
],
style={
    'background': colors['background'],
    'minHeight': '100vh',
    'fontFamily': 'Segoe UI, Arial'
})

@app.callback(
    Output('prediction-output', 'children'),
    Input('submit-button', 'n_clicks'),
    [State('Product_Code', 'value'),
     State('Warehouse', 'value'),
     State('Product_Category', 'value'),
     State('Promo', 'value'),
     State('Petrol_price', 'value'),
     State('High_Demand', 'value')]
)
def update_output(n_clicks, product_code, warehouse, category, promo, petrol_price, high_demand):
    if n_clicks > 0:
        input_df = pd.DataFrame([[
            product_code,
            warehouse,
            category,
            promo,
            petrol_price,
            high_demand
        ]], columns=['Product_Code', 'Warehouse', 'Product_Category', 'Promo', 'Petrol_price', 'High_Demand'])
        
        prediction = model.predict(input_df)
        return f'Predicted Production: {prediction[0]:.2f} units'
    return ''

if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=False)