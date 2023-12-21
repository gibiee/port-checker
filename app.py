import gradio as gr
import socket

def check(ip, port) :
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s :
        resp = s.connect_ex((ip, int(port)))

    if resp == 0 :
        return 'Opened'
    elif resp == 10061 :
        return 'Opened but nothing'
    elif resp == 10060 :
        return 'Closed'
    else :
        return "Unknown"

with gr.Blocks() as demo :
    gr.Markdown("""
                # Port Checker
                ### Output will be returned one of the 4 states.
                ① Opened  
                ② Opened but nothing  
                ③ Closed  
                ④ Unknown  
                """)
    with gr.Row() :
        with gr.Column() :
            input_ip = gr.Text(label='ip', value="127.0.0.1")
            input_port = gr.Text(label='port', value="80")
            btn = gr.Button(value="Check", variant='primary')
        
        with gr.Column() :
            output_state = gr.Text(label='state', interactive=False)

    btn.click(fn=check, inputs=[input_ip, input_port], outputs=output_state)

demo.launch()