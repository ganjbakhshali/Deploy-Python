namespace RandomFoodAPI_Csharp
{
    partial class Form1
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.btn_getPic = new System.Windows.Forms.Button();
            this.lbl_foodName = new System.Windows.Forms.Label();
            this.pbox_food = new System.Windows.Forms.PictureBox();
            ((System.ComponentModel.ISupportInitialize)(this.pbox_food)).BeginInit();
            this.SuspendLayout();
            // 
            // btn_getPic
            // 
            this.btn_getPic.Location = new System.Drawing.Point(60, 51);
            this.btn_getPic.Name = "btn_getPic";
            this.btn_getPic.Size = new System.Drawing.Size(427, 23);
            this.btn_getPic.TabIndex = 0;
            this.btn_getPic.Text = "Get Random Food Picture";
            this.btn_getPic.UseVisualStyleBackColor = true;
            this.btn_getPic.Click += new System.EventHandler(this.btn_getPic_Click);
            // 
            // lbl_foodName
            // 
            this.lbl_foodName.AutoSize = true;
            this.lbl_foodName.Location = new System.Drawing.Point(239, 108);
            this.lbl_foodName.Name = "lbl_foodName";
            this.lbl_foodName.Size = new System.Drawing.Size(0, 15);
            this.lbl_foodName.TabIndex = 1;
            // 
            // pbox_food
            // 
            this.pbox_food.Location = new System.Drawing.Point(101, 186);
            this.pbox_food.Name = "pbox_food";
            this.pbox_food.Size = new System.Drawing.Size(340, 362);
            this.pbox_food.TabIndex = 2;
            this.pbox_food.TabStop = false;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(7F, 15F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(551, 627);
            this.Controls.Add(this.pbox_food);
            this.Controls.Add(this.lbl_foodName);
            this.Controls.Add(this.btn_getPic);
            this.Name = "Form1";
            this.Text = "Raondom Food Picture";
            ((System.ComponentModel.ISupportInitialize)(this.pbox_food)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private Button btn_getPic;
        private Label lbl_foodName;
        private PictureBox pbox_food;
    }
}