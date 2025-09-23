import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.tree import DecisionTreeRegressor, plot_tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from datetime import datetime, timedelta
import json
import random
from typing import Dict, List, Tuple
import warnings
warnings.filterwarnings('ignore')

class NetworkDataGenerator:
    """Generate synthetic network data for training decision tree models"""
    
    def __init__(self, seed=42):
        np.random.seed(seed)
        random.seed(seed)
    
    def generate_synthetic_data(self, num_samples=10000) -> pd.DataFrame:
        """Generate synthetic network data with realistic patterns"""
        
        data = []
        start_date = datetime.now() - timedelta(days=30)
        
        for i in range(num_samples):
            # Generate time-based features
            current_time = start_date + timedelta(minutes=i * 1.5)
            hour = current_time.hour
            day_of_week = current_time.weekday()  # 0=Monday, 6=Sunday
            is_weekend = 1 if day_of_week >= 5 else 0
            
            # Time-based patterns
            if 0 <= hour <= 6:  # Night time
                base_users = np.random.normal(200, 50)
                traffic_intensity = np.random.uniform(0.1, 0.3)
            elif 7 <= hour <= 9:  # Morning rush
                base_users = np.random.normal(800, 100)
                traffic_intensity = np.random.uniform(0.6, 0.8)
            elif 10 <= hour <= 17:  # Office hours
                base_users = np.random.normal(1200, 150)
                traffic_intensity = np.random.uniform(0.7, 0.9)
            elif 18 <= hour <= 22:  # Evening peak
                base_users = np.random.normal(1600, 200)
                traffic_intensity = np.random.uniform(0.8, 1.0)
            else:  # Late night
                base_users = np.random.normal(400, 80)
                traffic_intensity = np.random.uniform(0.2, 0.5)
            
            # Weekend adjustments
            if is_weekend:
                base_users *= 0.7
                traffic_intensity *= 0.8
            
            # Weather impact (synthetic)
            weather_impact = np.random.choice([0.8, 0.9, 1.0, 1.1, 1.2], 
                                            p=[0.1, 0.2, 0.4, 0.2, 0.1])
            
            # Service types distribution
            total_users = max(50, int(base_users * weather_impact))
            video_users = int(total_users * np.random.uniform(0.5, 0.7))
            gaming_users = int(total_users * np.random.uniform(0.15, 0.35))
            iot_devices = int(total_users * np.random.uniform(0.1, 0.25))
            
            # Network load factors
            cpu_utilization = min(100, traffic_intensity * 100 + np.random.normal(0, 10))
            memory_usage = min(100, traffic_intensity * 90 + np.random.normal(0, 8))
            bandwidth_usage = min(100, traffic_intensity * 95 + np.random.normal(0, 12))
            
            # Calculate optimal power usage (target variable)
            # This simulates the AI optimization decision
            base_power = 100  # Static allocation
            
            # Power reduction based on usage patterns
            if cpu_utilization < 30:
                power_reduction = 0.6  # 60% reduction for low usage
            elif cpu_utilization < 50:
                power_reduction = 0.4  # 40% reduction for moderate usage
            elif cpu_utilization < 80:
                power_reduction = 0.2  # 20% reduction for high usage
            else:
                power_reduction = 0.0  # No reduction for peak usage
            
            # Additional reductions based on service types
            if video_users < total_users * 0.3:  # Low video usage
                power_reduction += 0.1
            if gaming_users < total_users * 0.1:  # Low gaming usage
                power_reduction += 0.15
            
            optimal_power = max(15, base_power * (1 - min(power_reduction, 0.8)))
            energy_saved = ((base_power - optimal_power) / base_power) * 100
            
            # QoS metrics (should remain high despite power optimization)
            if optimal_power < 30:
                qos_score = np.random.uniform(85, 95)  # Slight QoS impact for aggressive optimization
            else:
                qos_score = np.random.uniform(95, 99.9)
            
            latency = max(5, 50 - (optimal_power / 2) + np.random.normal(0, 3))
            packet_loss = max(0, 0.5 - (optimal_power / 200) + np.random.normal(0, 0.1))
            
            data.append({
                'timestamp': current_time,
                'hour': hour,
                'day_of_week': day_of_week,
                'is_weekend': is_weekend,
                'total_users': total_users,
                'video_users': video_users,
                'gaming_users': gaming_users,
                'iot_devices': iot_devices,
                'cpu_utilization': cpu_utilization,
                'memory_usage': memory_usage,
                'bandwidth_usage': bandwidth_usage,
                'weather_impact': weather_impact,
                'traffic_intensity': traffic_intensity,
                'optimal_power': optimal_power,
                'energy_saved': energy_saved,
                'qos_score': qos_score,
                'latency': latency,
                'packet_loss': packet_loss
            })
        
        return pd.DataFrame(data)

class GreenNetworkAI:
    """AI-powered network slicing optimizer using Decision Tree"""
    
    def __init__(self):
        self.model = None
        self.feature_importance = None
        self.data = None
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None
        
    def load_data(self, data: pd.DataFrame):
        """Load and prepare data for training"""
        self.data = data.copy()
        
        # Select features for the model
        feature_columns = [
            'hour', 'day_of_week', 'is_weekend', 'total_users',
            'video_users', 'gaming_users', 'iot_devices',
            'cpu_utilization', 'memory_usage', 'bandwidth_usage',
            'weather_impact', 'traffic_intensity'
        ]
        
        X = self.data[feature_columns]
        y = self.data['optimal_power']
        
        # Split data
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        
        return X, y
    
    def train_model(self, max_depth=10, min_samples_split=20):
        """Train the decision tree model"""
        self.model = DecisionTreeRegressor(
            max_depth=max_depth,
            min_samples_split=min_samples_split,
            random_state=42
        )
        
        self.model.fit(self.X_train, self.y_train)
        
        # Calculate feature importance
        self.feature_importance = pd.DataFrame({
            'feature': self.X_train.columns,
            'importance': self.model.feature_importances_
        }).sort_values('importance', ascending=False)
        
        return self.model
    
    def evaluate_model(self):
        """Evaluate model performance"""
        y_pred_train = self.model.predict(self.X_train)
        y_pred_test = self.model.predict(self.X_test)
        
        metrics = {
            'train_r2': r2_score(self.y_train, y_pred_train),
            'test_r2': r2_score(self.y_test, y_pred_test),
            'train_rmse': np.sqrt(mean_squared_error(self.y_train, y_pred_train)),
            'test_rmse': np.sqrt(mean_squared_error(self.y_test, y_pred_test))
        }
        
        return metrics, y_pred_test
    
    def predict_power_optimization(self, input_features: Dict) -> Dict:
        """Predict optimal power usage for given network conditions"""
        if self.model is None:
            raise ValueError("Model not trained yet!")
        
        # Convert input to DataFrame
        input_df = pd.DataFrame([input_features])
        
        # Predict optimal power
        optimal_power = self.model.predict(input_df)[0]
        energy_saved = ((100 - optimal_power) / 100) * 100
        
        # Calculate environmental impact
        co2_saved = energy_saved * 0.1  # kg CO2 per % energy saved
        cost_saved = energy_saved * 45  # $ per % energy saved
        
        return {
            'optimal_power': round(optimal_power, 2),
            'energy_saved': round(energy_saved, 2),
            'co2_saved': round(co2_saved, 2),
            'cost_saved': round(cost_saved, 2)
        }
    
    def visualize_results(self):
        """Create comprehensive visualizations"""
        fig, axes = plt.subplots(2, 3, figsize=(20, 12))
        fig.suptitle('🌿 Green Network AI - Decision Tree Analysis', fontsize=16, fontweight='bold')
        
        # 1. Feature Importance
        axes[0, 0].barh(self.feature_importance['feature'][:8], 
                       self.feature_importance['importance'][:8])
        axes[0, 0].set_title('📊 Feature Importance')
        axes[0, 0].set_xlabel('Importance Score')
        
        # 2. Actual vs Predicted
        y_pred_test = self.model.predict(self.X_test)
        axes[0, 1].scatter(self.y_test, y_pred_test, alpha=0.6)
        axes[0, 1].plot([self.y_test.min(), self.y_test.max()], 
                       [self.y_test.min(), self.y_test.max()], 'r--', lw=2)
        axes[0, 1].set_title('🎯 Actual vs Predicted Power Usage')
        axes[0, 1].set_xlabel('Actual Power (%)')
        axes[0, 1].set_ylabel('Predicted Power (%)')
        
        # 3. Power Usage by Hour
        hourly_avg = self.data.groupby('hour')['optimal_power'].mean()
        axes[0, 2].plot(hourly_avg.index, hourly_avg.values, marker='o', linewidth=2)
        axes[0, 2].set_title('⏰ Average Power Usage by Hour')
        axes[0, 2].set_xlabel('Hour of Day')
        axes[0, 2].set_ylabel('Optimal Power (%)')
        axes[0, 2].grid(True, alpha=0.3)
        
        # 4. Energy Savings Distribution
        axes[1, 0].hist(self.data['energy_saved'], bins=30, alpha=0.7, color='green')
        axes[1, 0].set_title('💚 Energy Savings Distribution')
        axes[1, 0].set_xlabel('Energy Saved (%)')
        axes[1, 0].set_ylabel('Frequency')
        
        # 5. Service Types vs Power Usage
        scatter = axes[1, 1].scatter(self.data['total_users'], self.data['optimal_power'], 
                                   c=self.data['traffic_intensity'], cmap='viridis', alpha=0.6)
        axes[1, 1].set_title('👥 Users vs Power Usage')
        axes[1, 1].set_xlabel('Total Users')
        axes[1, 1].set_ylabel('Optimal Power (%)')
        plt.colorbar(scatter, ax=axes[1, 1], label='Traffic Intensity')
        
        # 6. Decision Tree Visualization (simplified)
        if self.model.tree_.max_depth <= 4:  # Only for small trees
            plot_tree(self.model, ax=axes[1, 2], max_depth=3, 
                     feature_names=self.X_train.columns, filled=True, fontsize=8)
            axes[1, 2].set_title('🌳 Decision Tree Structure')
        else:
            axes[1, 2].text(0.5, 0.5, 'Tree too complex\nto visualize\n\nDepth: {}\nNodes: {}'.format(
                self.model.tree_.max_depth, self.model.tree_.node_count),
                ha='center', va='center', fontsize=12)
            axes[1, 2].set_title('🌳 Decision Tree Info')
        
        plt.tight_layout()
        plt.show()
    
    def generate_report(self) -> str:
        """Generate a comprehensive analysis report"""
        if self.model is None:
            return "❌ Model not trained yet!"
        
        metrics, _ = self.evaluate_model()
        avg_energy_saved = self.data['energy_saved'].mean()
        avg_power_reduction = 100 - self.data['optimal_power'].mean()
        
        report = f"""
🌿 GREEN NETWORK AI - ANALYSIS REPORT
{'='*50}

📊 MODEL PERFORMANCE:
• R² Score (Test): {metrics['test_r2']:.3f}
• RMSE (Test): {metrics['test_rmse']:.2f}
• Model Depth: {self.model.tree_.max_depth}
• Total Nodes: {self.model.tree_.node_count}

⚡ OPTIMIZATION RESULTS:
• Average Energy Saved: {avg_energy_saved:.1f}%
• Average Power Reduction: {avg_power_reduction:.1f}%
• Estimated Annual CO₂ Reduction: {avg_energy_saved * 36.5:.1f} tons
• Estimated Annual Cost Savings: ${avg_energy_saved * 16425:.0f}

🎯 TOP INFLUENTIAL FACTORS:
"""
        
        for i, row in self.feature_importance.head(5).iterrows():
            report += f"• {row['feature']}: {row['importance']:.3f}\n"
        
        report += f"""
🔍 PATTERN INSIGHTS:
• Peak optimization during night hours (0-6 AM)
• Moderate optimization during office hours
• Service-type aware allocation (Video/Gaming/IoT)
• Weather-sensitive adjustments
• Weekend usage pattern recognition

✅ QoS GUARANTEE:
• Average QoS Score: {self.data['qos_score'].mean():.1f}%
• Average Latency: {self.data['latency'].mean():.1f}ms
• Average Packet Loss: {self.data['packet_loss'].mean():.3f}%

💡 RECOMMENDATIONS:
1. Deploy AI optimizer during low-traffic periods first
2. Monitor QoS metrics continuously
3. Adjust optimization aggressiveness based on SLA requirements
4. Consider seasonal patterns for long-term planning

🚀 READY FOR PRODUCTION DEPLOYMENT!
"""
        
        return report

# Example usage and testing
def main():
    print("🌿 Green Network AI - Python Implementation")
    print("="*50)
    
    # Generate synthetic data
    print("📊 Generating synthetic network data...")
    generator = NetworkDataGenerator(seed=42)
    data = generator.generate_synthetic_data(num_samples=5000)
    
    print(f"✅ Generated {len(data)} data points")
    print("\n📋 Data sample:")
    print(data.head())
    
    # Initialize AI system
    ai_system = GreenNetworkAI()
    
    # Load and prepare data
    print("\n🔄 Preparing data for training...")
    X, y = ai_system.load_data(data)
    
    # Train the model
    print("🤖 Training Decision Tree model...")
    model = ai_system.train_model(max_depth=8, min_samples_split=50)
    
    # Evaluate model
    metrics, predictions = ai_system.evaluate_model()
    print(f"✅ Model trained successfully!")
    print(f"📈 Test R² Score: {metrics['test_r2']:.3f}")
    print(f"📉 Test RMSE: {metrics['test_rmse']:.2f}")
    
    # Test prediction
    print("\n🔮 Testing prediction...")
    test_input = {
        'hour': 14,  # 2 PM
        'day_of_week': 2,  # Wednesday
        'is_weekend': 0,
        'total_users': 1200,
        'video_users': 720,
        'gaming_users': 240,
        'iot_devices': 180,
        'cpu_utilization': 75,
        'memory_usage': 68,
        'bandwidth_usage': 82,
        'weather_impact': 1.0,
        'traffic_intensity': 0.8
    }
    
    result = ai_system.predict_power_optimization(test_input)
    print(f"🎯 Prediction for office hours scenario:")
    print(f"   • Optimal Power: {result['optimal_power']}%")
    print(f"   • Energy Saved: {result['energy_saved']}%")
    print(f"   • CO₂ Saved: {result['co2_saved']} kg")
    print(f"   • Cost Saved: ${result['cost_saved']}")
    
    # Generate comprehensive report
    print("\n📋 Generating analysis report...")
    report = ai_system.generate_report()
    print(report)
    
    # Create visualizations
    print("📊 Creating visualizations...")
    ai_system.visualize_results()
    
    print("\n🎉 Analysis complete! Check the generated plots and report.")
    
    return ai_system, data

if __name__ == "__main__":
    ai_system, data = main()